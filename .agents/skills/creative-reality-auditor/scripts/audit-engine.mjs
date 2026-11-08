#!/usr/bin/env node
/**
 * Creative Reality Auditor (CRA) - Core Execution Engine
 * Pure Node.js (ESM), zero extra dependencies.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const SKILL_ROOT = path.resolve(__dirname, '..');

// Helper to read files safely
export function readFileSafe(filePath) {
  return fs.readFileSync(filePath, 'utf8');
}

// Simple YAML parser for profile files (flat keys, nested weights & maps)
export function parseProfileYaml(content) {
  const result = {
    weights: {},
    criteria_map: {},
    mandatory_judges: [],
    conditional_judges: {},
    critical_failure_triggers: []
  };

  const lines = content.split(/\r?\n/);
  let currentSection = null;
  let currentSubKey = null;

  for (const rawLine of lines) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) continue;

    if (line.startsWith('profile_id:')) {
      result.profile_id = line.replace('profile_id:', '').trim();
    } else if (line.startsWith('name:')) {
      result.name = line.replace('name:', '').trim().replace(/^["']|["']$/g, '');
    } else if (line.startsWith('description:')) {
      result.description = line.replace('description:', '').trim().replace(/^["']|["']$/g, '');
    } else if (line.startsWith('target_work_type:')) {
      result.target_work_type = line.replace('target_work_type:', '').trim();
    } else if (line.startsWith('default_world_mode:')) {
      result.default_world_mode = line.replace('default_world_mode:', '').trim();
    } else if (line.startsWith('weights:')) {
      currentSection = 'weights';
    } else if (line.startsWith('criteria_map:')) {
      currentSection = 'criteria_map';
    } else if (line.startsWith('mandatory_judges:')) {
      currentSection = 'mandatory_judges';
    } else if (line.startsWith('conditional_judges:')) {
      currentSection = 'conditional_judges';
    } else if (line.startsWith('critical_failure_triggers:')) {
      currentSection = 'critical_failure_triggers';
    } else if (currentSection === 'weights' && /^[a-zA-Z0-9_]+:\s*\d+/.test(line)) {
      const [k, v] = line.split(':').map(s => s.trim());
      result.weights[k] = parseInt(v, 10);
    } else if (currentSection === 'mandatory_judges' && line.startsWith('-')) {
      result.mandatory_judges.push(line.replace('-', '').trim());
    } else if (currentSection === 'critical_failure_triggers' && line.startsWith('-')) {
      result.critical_failure_triggers.push(line.replace('-', '').trim());
    } else if (currentSection === 'conditional_judges' && line.includes(':')) {
      const idx = line.indexOf(':');
      const k = line.slice(0, idx).trim();
      const v = line.slice(idx + 1).trim().replace(/^["']|["']$/g, '');
      result.conditional_judges[k] = v;
    } else if (currentSection === 'criteria_map') {
      if (rawLine.startsWith('  ') && !rawLine.startsWith('    ') && line.endsWith(':')) {
        currentSubKey = line.replace(':', '').trim();
        result.criteria_map[currentSubKey] = {};
      } else if (rawLine.startsWith('    ') && currentSubKey && line.includes(':')) {
        const idx = line.indexOf(':');
        const k = line.slice(0, idx).trim();
        const v = line.slice(idx + 1).trim().replace(/^["']|["']$/g, '');
        result.criteria_map[currentSubKey][k] = v;
      }
    }
  }

  return result;
}

// Load profile for a given work_type
export function loadProfile(workType) {
  const profilePath = path.join(SKILL_ROOT, 'profiles', `${workType}.yaml`);
  if (!fs.existsSync(profilePath)) {
    throw new Error(`Profile not found for work_type: ${workType} at ${profilePath}`);
  }
  return parseProfileYaml(readFileSafe(profilePath));
}

// Compute audit report deterministically given evaluation data
export function evaluateAudit(inputData, evaluation) {
  const profile = loadProfile(inputData.work_type);
  const weights = { ...profile.weights, ...(inputData.weights_override || {}) };

  // Calculate score breakdown
  const scoreBreakdown = [];
  let totalScore = 0;
  let totalWeight = 0;

  for (const [criterion, weight] of Object.entries(weights)) {
    const rawScore = evaluation.scores?.[criterion] ?? 7.0; // default 7/10 if not scored
    const maxScore = 10.0;
    const weightedScore = (rawScore / maxScore) * weight;
    totalScore += weightedScore;
    totalWeight += weight;

    const summary = evaluation.criterion_summaries?.[criterion] ||
      profile.criteria_map?.[criterion]?.description || 'Evaluated against criteria standards.';

    scoreBreakdown.push({
      criterion,
      score: Math.round(rawScore * 10) / 10,
      max_score: maxScore,
      weight,
      weighted_score: Math.round(weightedScore * 10) / 10,
      evidence_summary: summary
    });
  }

  // Normalize if weights don't sum to 100
  if (totalWeight > 0 && Math.abs(totalWeight - 100) > 0.01) {
    totalScore = (totalScore / totalWeight) * 100;
  }
  totalScore = Math.round(totalScore * 10) / 10;

  // Process issues and check for critical failures
  const issues = evaluation.issues || [];
  const criticalFailures = [];
  let hasCriticalFail = false;

  for (const issue of issues) {
    if (issue.severity === 'CRITICAL') {
      hasCriticalFail = true;
      criticalFailures.push({
        id: issue.id || `CRIT-${criticalFailures.length + 1}`,
        issue: issue.problem,
        evidence: issue.evidence,
        location: issue.location,
        confirmed: true,
        veto_rule: 'Truth Over Consensus (Veto overrides majority score)'
      });
    }
  }

  // Determine final verdict
  let verdict = 'PASS';
  let verdictReason = 'Meets or exceeds all creative reality and logic standards.';

  if (evaluation.insufficient_evidence) {
    verdict = 'INSUFFICIENT_EVIDENCE';
    verdictReason = evaluation.insufficient_evidence_reason || 'Essential assets or text required for evaluation are missing.';
  } else if (hasCriticalFail) {
    if (criticalFailures.length >= 3) {
      verdict = 'REJECT';
      verdictReason = `Multiple critical failures (${criticalFailures.length}) detected that invalidate core project logic.`;
    } else {
      verdict = 'REVISE';
      verdictReason = `Contains ${criticalFailures.length} confirmed critical failure(s) that must be resolved, notwithstanding total score of ${totalScore}.`;
    }
  } else if (totalScore < 70) {
    verdict = 'REVISE';
    verdictReason = `Overall score ${totalScore}/100 is below the passing threshold (70/100).`;
  } else if (totalScore < 80) {
    verdict = 'PASS_WITH_NOTES';
    verdictReason = `Overall score ${totalScore}/100 meets baseline requirements with minor issues to address.`;
  } else {
    verdict = 'PASS';
    verdictReason = `High quality submission (${totalScore}/100) with no blocking issues.`;
  }

  const passed = (verdict === 'PASS' || verdict === 'PASS_WITH_NOTES');

  // Prepare revision plan
  const revisionPlan = evaluation.revision_plan || [];
  if (revisionPlan.length === 0 && issues.length > 0) {
    issues.forEach((issue, idx) => {
      let priority = 'P2_MEDIUM';
      if (issue.severity === 'CRITICAL') priority = 'P0_CRITICAL';
      else if (issue.severity === 'HIGH') priority = 'P1_HIGH';
      else if (issue.severity === 'LOW' || issue.severity === 'INFO') priority = 'P3_POLISH';

      revisionPlan.push({
        step: idx + 1,
        priority,
        target_location: issue.location,
        action: issue.suggested_fix,
        rationale: issue.why_it_matters
      });
    });
  }

  const auditId = evaluation.audit_id || `CRA-${Date.now().toString(36).toUpperCase()}`;
  const timestamp = new Date().toISOString();

  return {
    audit_id: auditId,
    timestamp,
    title: inputData.title,
    work_type: inputData.work_type,
    world_mode: inputData.world_mode || profile.default_world_mode || 'realistic',
    verdict,
    verdict_reason: verdictReason,
    total_score: totalScore,
    passed,
    has_critical_fail: hasCriticalFail,
    critical_failures: criticalFailures,
    score_breakdown: scoreBreakdown,
    issues,
    judge_opinions: evaluation.judge_opinions || {},
    debate_summary: evaluation.debate_summary || [],
    unverified_claims: evaluation.unverified_claims || [],
    revision_plan: revisionPlan,
    revised_draft: evaluation.revised_draft || null,
    human_override: evaluation.human_override || null
  };
}

// Format the final report into clean GitHub-flavored Markdown
export function formatMarkdownReport(report) {
  let template = readFileSafe(path.join(SKILL_ROOT, 'templates', 'quality-report.md'));

  template = template.replace('{{AUDIT_ID}}', report.audit_id);
  template = template.replace('{{TIMESTAMP}}', report.timestamp);
  template = template.replace('{{TITLE}}', report.title);
  template = template.replace('{{WORK_TYPE}}', report.work_type);
  template = template.replace('{{WORLD_MODE}}', report.world_mode);
  template = template.replace('{{VERDICT}}', report.verdict);
  template = template.replace('{{TOTAL_SCORE}}', String(report.total_score));
  template = template.replace('{{VERDICT_REASON}}', report.verdict_reason);
  template = template.replace('{{CRITICAL_FAIL_STATUS}}', report.has_critical_fail ? '❌ พบข้อผิดพลาดร้ายแรง' : '✅ ผ่าน (ไม่พบข้อผิดพลาดวิกฤต)');
  template = template.replace('{{EVIDENCE_STATUS}}', report.verdict === 'INSUFFICIENT_EVIDENCE' ? '⚠️ ข้อมูลไม่เพียงพอ' : '✅ ครบถ้วน');

  // Breakdown rows
  const breakdownRows = report.score_breakdown.map(item =>
    `| **${item.criterion}** | - | ${item.weight}% | ${item.score} | ${item.weighted_score} | ${item.evidence_summary} |`
  ).join('\n');
  template = template.replace('{{SCORE_BREAKDOWN_ROWS}}', breakdownRows);

  // Issue list
  let issueText = '';
  if (report.issues.length === 0) {
    issueText = '_ไม่พบข้อผิดพลาดที่ต้องบันทึก (No issues detected)_';
  } else {
    issueText = report.issues.map(iss => {
      return `#### [${iss.severity}] ${iss.problem} (${iss.id || 'ISSUE'})\n` +
        `- **ตำแหน่ง:** \`${iss.location}\` | **กรรมการ:** \`${iss.judge}\` | **ความมั่นใจ:** ${iss.confidence || 'HIGH'}\n` +
        `- **หลักฐาน:** ${iss.evidence}\n` +
        `- **เหตุผลที่กระทบ:** ${iss.why_it_matters}\n` +
        `- **คำแนะนำแก้ไข (Minimal Fix):** ${iss.suggested_fix}\n` +
        (iss.alternative_fix ? `- **ทางเลือกสำรอง:** ${iss.alternative_fix}\n` : '');
    }).join('\n');
  }
  template = template.replace('{{ISSUE_LIST}}', issueText);

  // Debate summary
  let debateText = '';
  if (report.debate_summary.length === 0) {
    debateText = '_กรรมการทุกท่านมีความเห็นสอดคล้องกันบนหลักฐานเชิงประจักษ์_';
  } else {
    debateText = report.debate_summary.map(d =>
      `- **ประเด็น:** ${d.topic}\n  - *Devil's Advocate ท้าทาย:* ${d.advocate_challenge}\n  - *คำชี้แจง:* ${d.judge_defense}\n  - *ข้อยุติของ Chief Judge:* ${d.resolution}`
    ).join('\n\n');
  }
  template = template.replace('{{DEBATE_SUMMARY}}', debateText);

  // Revision plan
  let revisionText = '';
  if (report.revision_plan.length === 0) {
    revisionText = '_ไม่ต้องแก้ไข สามารถเข้าสู่กระบวนการผลิตต่อไปได้ทันที_';
  } else {
    revisionText = report.revision_plan.map(r =>
      `| **${r.step}** | \`${r.priority}\` | \`${r.target_location}\` | ${r.action} | ${r.suggested_text || '-'} | ${r.rationale} |`
    ).join('\n');
    revisionText = `| ลำดับ | ระดับความสำคัญ | ตำแหน่งเป้าหมาย | มาตรการแก้ไข | ตัวอย่างการแก้ | เหตุผล |\n| :---: | :--- | :--- | :--- | :--- | :--- |\n` + revisionText;
  }
  template = template.replace('{{REVISION_PLAN_STEPS}}', revisionText);

  return template;
}

// CLI entry point
if (process.argv[1] === fileURLToPath(import.meta.url)) {
  const args = process.argv.slice(2);
  const command = args[0] || 'help';

  if (command === 'audit') {
    const inputPath = args[1];
    if (!inputPath || !fs.existsSync(inputPath)) {
      console.error(`Error: Input file required. Found: ${inputPath}`);
      process.exit(1);
    }
    const rawInput = JSON.parse(readFileSafe(inputPath));
    const evalData = rawInput.evaluation || rawInput;
    const report = evaluateAudit(rawInput, evalData);

    const outJsonIdx = args.indexOf('--output-json');
    if (outJsonIdx !== -1 && args[outJsonIdx + 1]) {
      fs.writeFileSync(args[outJsonIdx + 1], JSON.stringify(report, null, 2), 'utf8');
      console.log(`Saved JSON report to ${args[outJsonIdx + 1]}`);
    }

    const outMdIdx = args.indexOf('--output-md');
    if (outMdIdx !== -1 && args[outMdIdx + 1]) {
      const md = formatMarkdownReport(report);
      fs.writeFileSync(args[outMdIdx + 1], md, 'utf8');
      console.log(`Saved Markdown report to ${args[outMdIdx + 1]}`);
    }

    console.log(`Audit Completed: [${report.verdict}] Total Score: ${report.total_score}/100 (Has Critical Fail: ${report.has_critical_fail})`);
  } else {
    console.log(`Usage: node scripts/audit-engine.mjs audit <input.json> [--output-json <path>] [--output-md <path>]`);
  }
}

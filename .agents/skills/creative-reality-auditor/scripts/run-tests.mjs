#!/usr/bin/env node
/**
 * Automated Test Runner for Creative Reality Auditor (CRA)
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { evaluateAudit, formatMarkdownReport } from './audit-engine.mjs';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const TESTS_DIR = path.resolve(__dirname, '..', 'tests');

function runAllTests() {
  const testFiles = fs.readdirSync(TESTS_DIR)
    .filter(f => f.endsWith('.json'))
    .sort();

  console.log(`\n======================================================`);
  console.log(`Running Creative Reality Auditor (CRA) Test Suite (${testFiles.length} cases)`);
  console.log(`======================================================\n`);

  let passedTests = 0;
  let failedTests = 0;

  for (const file of testFiles) {
    const fullPath = path.join(TESTS_DIR, file);
    const testData = JSON.parse(fs.readFileSync(fullPath, 'utf8'));

    try {
      const report = evaluateAudit(testData, testData.evaluation);

      // Verify expectations
      const expected = testData.expected || {};
      const errors = [];

      if (expected.verdict && report.verdict !== expected.verdict) {
        errors.push(`Verdict mismatch: expected '${expected.verdict}', got '${report.verdict}'`);
      }
      if (expected.has_critical_fail !== undefined && report.has_critical_fail !== expected.has_critical_fail) {
        errors.push(`Critical Fail mismatch: expected ${expected.has_critical_fail}, got ${report.has_critical_fail}`);
      }
      if (expected.passed !== undefined && report.passed !== expected.passed) {
        errors.push(`Passed status mismatch: expected ${expected.passed}, got ${report.passed}`);
      }

      if (errors.length === 0) {
        passedTests++;
        console.log(`✅ [PASS] ${testData.test_id || file}: ${testData.name}`);
        console.log(`   -> Verdict: ${report.verdict} | Total Score: ${report.total_score}/100 | Critical Fail: ${report.has_critical_fail}`);
      } else {
        failedTests++;
        console.error(`❌ [FAIL] ${testData.test_id || file}: ${testData.name}`);
        for (const err of errors) {
          console.error(`   -> ${err}`);
        }
      }
    } catch (err) {
      failedTests++;
      console.error(`❌ [ERROR] ${testData.test_id || file}: Exception thrown - ${err.message}`);
    }
  }

  console.log(`\n------------------------------------------------------`);
  console.log(`Test Results: ${passedTests} passed, ${failedTests} failed out of ${testFiles.length}`);
  console.log(`------------------------------------------------------\n`);

  if (failedTests > 0) {
    process.exit(1);
  }
}

runAllTests();

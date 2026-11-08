---
name: playwright-mcp
description: Automate real browsers with the Microsoft Playwright MCP server (@playwright/mcp, configured in BigO .mcp.json) — accessibility snapshots, ref-based clicks and typing, file uploads, waits, screenshots, console and network logs. Use for scripted web steps such as Suno or Flow uploads and app testing, or as the fallback when the built-in browser cannot do a step.
---

# Playwright MCP — Universal Browser Automation & Testing Skill
## Official Microsoft Playwright Model Context Protocol (`@playwright/mcp`)

Automate, inspect, scrape, and test web applications in real browser environments using the official Microsoft Playwright MCP server.

> [!IMPORTANT]
> **Universal Multi-Agent Standard (มาตรฐานรองรับ AI ทุกค่าย):**
> สกิลนี้ออกแบบให้เป็น **Model-Agnostic** และ **Agent-Agnostic** AI Agent ทุกค่าย (เช่น **Google Antigravity**, **Anthropic Claude Code / Claude Desktop**, **OpenAI ChatGPT / Codex**, **Cursor**, **Windsurf**, และ **LM Studio**) สามารถเรียกใช้และควบคุม Browser ผ่านเครื่องมือ Playwright MCP ได้อย่างเต็มประสิทธิภาพและมีมาตรฐานเดียวกัน

---

## 🚀 1. Overview & Key Advantages

Playwright MCP bridges Large Language Models with actual web browsers (Chromium, Firefox, WebKit, Edge). Unlike traditional computer-use tools that rely on continuous full-resolution vision screenshots (which consume massive token budgets and struggle with pixel coordinates), Playwright MCP operates primarily on **Structured Accessibility Snapshots**:

1. **Token Efficiency:** Accessibility trees represent interactive DOM hierarchies in clean YAML/text format, saving up to 80-90% of tokens compared to base64 images.
2. **Deterministic Targeting:** Every interactive element is tagged with a unique `ref` ID (e.g. `ref="e12"`). AI models interact directly using references rather than guessing coordinate pixels.
3. **Responsive Resilience:** Interactions remain stable regardless of window resizing, DPI scaling, or responsive layout shifts.
4. **Full Browser Diagnostics:** Access live console messages, network request logs, request headers/bodies, and custom JavaScript evaluation in the page context.

---

## 🛠️ 2. Playwright MCP Toolset (25 Core Tools)

When the Playwright MCP server is active, it exposes 25 specialized browser tools:

### A. Navigation & Tab Management
| Tool | Description |
| :--- | :--- |
| `browser_navigate` | Navigates the current page to the target URL. |
| `browser_navigate_back` | Navigates back in the browser history. |
| `browser_tabs` | Lists, creates, closes, or switches between multiple browser tabs. |
| `browser_close` | Closes the current page/session. |

### B. Element Discovery & Snapshots (Preferred Workflow)
| Tool | Description |
| :--- | :--- |
| `browser_snapshot` | Captures the structured accessibility tree of the page. Returns interactive elements with their role, name, and `ref` ID. |
| `browser_find` | Searches the accessibility snapshot for specific text or regular expression. Cheaper than a full snapshot when locating a single control. |

### C. Interactions & Form Controls
| Tool | Description |
| :--- | :--- |
| `browser_click` | Clicks an element by `element` (ref) or locator. Supports double clicks, right clicks, and modifier keys. |
| `browser_type` | Types text into an editable input element identified by `element` (ref). |
| `browser_fill_form` | Fills multiple form inputs in a single call (e.g., username, password, checkboxes). |
| `browser_select_option`| Selects one or multiple options in a dropdown `<select>` element. |
| `browser_press_key` | Dispatches keyboard key events (e.g., `Enter`, `Tab`, `ArrowDown`, `Control+A`). |
| `browser_hover` | Hovers the cursor over a specific element (triggers tooltip / hover state). |
| `browser_drag` | Drags one element and drops it onto another element target. |
| `browser_file_upload` | Injects local file paths into a file input `<input type="file">`. |
| `browser_drop` | Simulates dropping external files or data directly onto a dropzone. |

### D. Synchronization & Dialogs
| Tool | Description |
| :--- | :--- |
| `browser_wait_for` | Pauses execution until specified text appears or disappears, or for a duration. |
| `browser_handle_dialog`| Dismisses or accepts browser dialogs (alert, confirm, prompt). |

### E. Visual Verification & Layout
| Tool | Description |
| :--- | :--- |
| `browser_take_screenshot` | Captures a PNG/JPEG screenshot of the current page or specific element. Use for visual verification. |
| `browser_resize` | Resizes the browser viewport (width and height in pixels). |
| `browser_emulate_media`| Toggles CSS media features (e.g. `colorScheme: "dark"` vs `"light"`, print media). |

### F. Network, Console & Advanced Code Execution
| Tool | Description |
| :--- | :--- |
| `browser_console_messages` | Retrieves runtime console logs (`error`, `warning`, `info`, `debug`). |
| `browser_network_requests` | Lists network requests executed since page load with status and timing. |
| `browser_network_request` | Retrieves full headers and payload of an individual network request by index. |
| `browser_evaluate` | Evaluates arbitrary JavaScript in the page DOM context and returns the result. |
| `browser_run_code_unsafe`| Runs arbitrary Playwright Node.js script in the server process. |

---

## 📋 3. Standard Operational Playbook

Always follow this 5-step loop when executing browser tasks:

```
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│ 1. Navigate     │ ──► │ 2. Snapshot/Find │ ──► │ 3. Act by Ref    │
│ browser_navigate│     │ browser_snapshot │     │ browser_click    │
└─────────────────┘     └──────────────────┘     └──────────────────┘
                                                          │
                        ┌──────────────────┐              ▼
                        │ 5. Verify / QA   │ ◄── ┌──────────────────┐
                        │ screenshot/eval  │     │ 4. Wait / Settle │
                        └──────────────────┘     │ browser_wait_for │
                                                 └──────────────────┘
```

### Step 1: Open Target URL
```json
{
  "tool": "browser_navigate",
  "arguments": { "url": "https://example.com/login" }
}
```

### Step 2: Inspect via Accessibility Snapshot
Instead of taking a screenshot, call `browser_snapshot`:
```json
{
  "tool": "browser_snapshot",
  "arguments": {}
}
```
*Output snippet:*
```yaml
- heading "Welcome Back" [level=1]
- textbox "Username" [ref=e3]
- textbox "Password" [ref=e4]
- button "Sign In" [ref=e5]
```

### Step 3: Perform Precise Action Using `ref`
Pass the `ref` directly to the action tool:
```json
{
  "tool": "browser_type",
  "arguments": { "element": "e3", "text": "agent_user" }
}
```
Or fill the whole form at once with `browser_fill_form`:
```json
{
  "tool": "browser_fill_form",
  "arguments": {
    "elements": [
      { "element": "e3", "value": "agent_user" },
      { "element": "e4", "value": "secret_password" }
    ]
  }
}
```
Then submit:
```json
{
  "tool": "browser_click",
  "arguments": { "element": "e5" }
}
```

### Step 4: Wait for State Transition
```json
{
  "tool": "browser_wait_for",
  "arguments": { "text": "Dashboard" }
}
```

### Step 5: Verification
* For data/status: Inspect the new snapshot with `browser_snapshot` or check `browser_console_messages`.
* For visual/layout signoff: Call `browser_take_screenshot` to confirm the final visual layout.

---

## ⚙️ 4. Multi-Agent Configuration Guide (AI ทุกค่าย)

### 1. Google Antigravity (Gemini CLI / IDE)
Stored in `~/.gemini/config/mcp_config.json`:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "cmd.exe",
      "args": ["/c", "npx", "-y", "@playwright/mcp@latest"]
    }
  }
}
```

### 2. Workspace Standard (`.mcp.json` — Cursor, Windsurf, VS Code, Claude Code)
Stored in project root `.mcp.json`:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "cmd.exe",
      "args": ["/c", "npx", "-y", "@playwright/mcp@latest"]
    }
  }
}
```

### 3. Claude Code / Claude Desktop
Global config `~/.claude/.mcp.json` or run:
```bash
claude mcp add playwright cmd.exe /c npx -y @playwright/mcp@latest
```

### 4. LM Studio
Stored in `~/.lmstudio/mcp.json`:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "cmd.exe",
      "args": ["/c", "npx", "-y", "@playwright/mcp@latest"]
    }
  }
}
```

---

## 💡 5. CLI Flags & Customizations

Customize the server by appending flags to the `args` array:

* **Headless Mode:** (Runs silently without popping up a window)
  `"args": ["/c", "npx", "-y", "@playwright/mcp@latest", "--headless"]`
* **Custom Browser Channel:**
  `"--browser=msedge"` or `"--browser=firefox"` or `"--browser=chrome"`
* **Save Session / Persistent Auth:**
  `"--storage-state=auth.json"` (preserves cookies across runs)
* **Mobile Viewport Emulation:**
  `"--mobile"` or `"--device=iPhone 15"`
* **Output Directory:**
  `"--output-dir=.playwright-mcp"` (stores screenshots and logs)

---

## 🏠 BigO rules (read before using Playwright here)

- **Uploads only from inside the project.** `browser_file_upload` accepts only files under
  `B:\ChatGPT\BigO`. Copy the files to `B:\ChatGPT\BigO\.playwright-mcp\<job>\`
  (git-ignored), upload from there and delete the copies when the job is done. Never upload
  from Downloads or another drive.
- **One shared profile.** The Playwright Chrome profile is shared with other sessions and
  keeps the owner's sign-ins (Google Flow was signed in as of Nov 2026; check each site's
  page before assuming). If it reports "Browser is already in use",
  another session holds it: ask the owner to close that window, or close it only when the
  owner asks. Do not delete the profile to "fix" it — that signs everything out.
- **Sign-ins stay with the owner.** If a site is signed out, ask the owner to sign in in the
  Playwright window; never type their password or switch accounts.
- **Captcha / verify pages: stop.** Shopee shows verify pages to automation even on simple
  reads; never try to pass a captcha. Report it and let the owner act.
- **Downloads** land in `.playwright-mcp/` or the browser's download folder; move every
  file into its project folder ([chatgpt-images](../chatgpt-images/SKILL.md) step 4).
- Site-specific steps: Flow in [google-flow](../google-flow/SKILL.md), Suno in
  [suno](../suno/SKILL.md).

---

## 🛡️ 6. Safety & Best Practices

1. **Avoid credential leakage:** Never commit plain-text credentials into scripts or logs. Use environment variables or `--secrets` files.
2. **Handle rate limits & bot protection:** Add appropriate timeouts (`--timeout-action=5000`). Never bypass Cloudflare/CAPTCHA or verify prompts — stop and hand the step to the owner.
3. **Session cleanup:** Always invoke `browser_close` when completing an automation sequence to free up GPU and system memory.

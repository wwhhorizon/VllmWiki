# vllm-project/vllm#35266: [Bug]: Missing opening brace for Qwen3.5 streaming tool calls

| 字段 | 值 |
| --- | --- |
| Issue | [#35266](https://github.com/vllm-project/vllm/issues/35266) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Missing opening brace for Qwen3.5 streaming tool calls

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `opencode` and `claudecode` with vllm (commit [3bbb20](https://github.com/vllm-project/vllm/commit/3bbb2046ff320395c80c139e55e7c1947c3fb5e1)), all tool calls fail: ``` ⚙ invalid [tool=bash, error=Invalid input for tool bash: JSON parsing failed: Text: "command": "export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && . \"$NVM_DIR/nvm.sh\" && nvm install 22", "description": "Install Node.js 22 via nvm", "timeout": 120000}. Error message: JSON Parse error: Unable to parse JSON string] ⚙ invalid [tool=bash, error=Invalid input for tool bash: JSON parsing failed: Text: "command": "export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && . \"$NVM_DIR/nvm.sh\" && nvm install 22", "description": "Install Node.js 22 via nvm", "timeout": 120000}. Error message: JSON Parse error: Unable to parse JSON string] ``` According to the text output , the tool call JSON is missing a opening brace "{". [Reproduction script](https://gist.github.com/AsterisMono/3e65fb181beb3cd088a2ce3b54ad330f) ```bash ❯ PYTHONPATH=$PWD /Users/nvirellia/Projects/vllm/.venv-codex/bin/python \ /Users/nvirellia/Projects/vllm/scripts/repro_qwen3co...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: OME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && . \"$NVM_DIR/nvm.sh\" && nvm install 22", "description": "Install Node.js 22 via nvm", "timeout": 120000}. Error message: JSON Parse error: Unable to parse JSON string] ⚙ inva...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: opening brace "{". [Reproduction script](https://gist.github.com/AsterisMono/3e65fb181beb3cd088a2ce3b54ad330f) ```bash ❯ PYTHONPATH=$PWD /Users/nvirellia/Projects/vllm/.venv-codex/bin/python \ /Users/nvirellia/Projects/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Missing opening brace for Qwen3.5 streaming tool calls bug;stale ### Your current environment ### 🐛 Describe the bug When using `opencode` and `claudecode` with vllm (commit [3bbb20](https://github.com/vllm-proje...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Missing opening brace for Qwen3.5 streaming tool calls bug;stale ### Your current environment ### 🐛 Describe the bug When using `opencode` and `claudecode` with vllm (commit [3bbb20](https://github.com/vllm-proje...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: cause platform detection to fail. INFO 02-25 14:14:20 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. INFO 02-25 14:14:24 [qwen3coder_tool_parser.py:85] vLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

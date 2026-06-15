# vllm-project/vllm#44148: [Bug]: Kimi 2.5 response formatting error / corrupted JSON output with huge whitespaces under high concurrency (H20)

| 字段 | 值 |
| --- | --- |
| Issue | [#44148](https://github.com/vllm-project/vllm/issues/44148) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Kimi 2.5 response formatting error / corrupted JSON output with huge whitespaces under high concurrency (H20)

### Issue 正文摘录

### Your current environment Hardware: 8 x NVIDIA H20 (96GB HBM3) Driver Version: 575.57.08 CUDA Version: 12.9 Model: Kimi 2.5 Startup Flags: --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 \ --enable-auto-tool-choice Concurrency: 5 concurrent requests ### 🐛 Describe the bug When running Kimi 2.5 under 5 concurrent requests with specific tool/reasoning parsers (kimi_k2), the model output becomes severely corrupted after a tool-use decision. Specifically, in the content field of the returned JSON, the model prints a brief introductory sentence and then triggers an abnormal stream of extensive hidden control characters (a massive mix of \t, \n, and spaces) instead of the actual response or tool execution text. { "reasoning": " 用户坚持要将 MD 转为 PDF，但当前环境确实缺少关键的 PDF 引擎（xelatex、wkhtmltopdf、typst、weasyprint 等都不存在），且 IE COM 对象也不可用。 I see the problems from the previous attempts: 1. No xelatex found 2. No wkhtmltopdf found 3. No markdown library in Python 4. IE COM object not registered (old Windows/IE removed) \n5. curl download of wkhtmltopdf didn't work properly (appears blocked or failed silently) The user wants MD→PDF specifically, so let me try a different approach. I should: 1....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: # Your current environment Hardware: 8 x NVIDIA H20 (96GB HBM3) Driver Version: 575.57.08 CUDA Version: 12.9 Model: Kimi 2.5 Startup Flags: --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 \ --enable-auto-tool-ch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: onment Hardware: 8 x NVIDIA H20 (96GB HBM3) Driver Version: 575.57.08 CUDA Version: 12.9 Model: Kimi 2.5 Startup Flags: --tool-call-parser kimi_k2 \ --reasoning-parser kimi_k2 \ --enable-auto-tool-choice Concurrency: 5...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Kimi 2.5 response formatting error / corrupted JSON output with huge whitespaces under high concurrency (H20) bug ### Your current environment Hardware: 8 x NVIDIA H20 (96GB HBM3) Driver Version: 575.57.08 CUDA V...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: \n5. curl download of wkhtmltopdf didn't work properly (appears blocked or failed silently) The user wants MD→PDF specifically, so let me try a different approach. I should:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ng-parser kimi_k2 \ --enable-auto-tool-choice Concurrency: 5 concurrent requests ### 🐛 Describe the bug When running Kimi 2.5 under 5 concurrent requests with specific tool/reasoning parsers (kimi_k2), the model output...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#22502: [Bug]: openai/gpt-oss-120b can't run on A100

| 字段 | 值 |
| --- | --- |
| Issue | [#22502](https://github.com/vllm-project/vllm/issues/22502) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;kernel |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: openai/gpt-oss-120b can't run on A100

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm following procedure to start vllm on A100: https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#a100 1. commands I used: ``` uv pip install --pre vllm==0.10.1+gptoss --extra-index-url https://wheels.vllm.ai/gpt-oss/ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 --index-strategy unsafe-best-match VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 CUDA_VISIBLE_DEVICES=1 vllm serve openai/gpt-oss-120b --async-scheduling --host 0.0.0.0 --port 8081 ``` 2. But I still get error: ``` (EngineCore_0 pid=29622) ERROR 08-07 23:07:34 [core.py:720] RuntimeError: Worker failed with error 'CUDA error: no kernel image is available for execution on the device ``` Could you please help to guide me what is wrong or is it a bug? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: llowing procedure to start vllm on A100: https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#a100 1. commands I used: ``` uv pip install --pre vllm==0.10.1+gptoss --extra-index-url https://wheels.vllm.ai...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: openai/gpt-oss-120b can't run on A100 bug ### Your current environment ### 🐛 Describe the bug I'm following procedure to start vllm on A100: https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#a10...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: /whl/nightly/cu128 --index-strategy unsafe-best-match VLLM_ATTENTION_BACKEND=TRITON_ATTN_VLLM_V1 CUDA_VISIBLE_DEVICES=1 vllm serve openai/gpt-oss-120b --async-scheduling --host 0.0.0.0 --port 8081 ``` 2. But I still get...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: openai/gpt-oss-120b can't run on A100 bug ### Your current environment ### 🐛 Describe the bug I'm following procedure to start vllm on A100: https://docs.vllm.ai/projects/recipes/en/latest/OpenAI/GPT-OSS.html#a10...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: hich can answer lots of frequently asked questions. development ci_build;scheduler_memory cuda;kernel env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

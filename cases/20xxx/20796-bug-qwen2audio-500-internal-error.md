# vllm-project/vllm#20796: [Bug]: Qwen2Audio 500 internal Error

| 字段 | 值 |
| --- | --- |
| Issue | [#20796](https://github.com/vllm-project/vllm/issues/20796) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2Audio 500 internal Error

### Issue 正文摘录

### Your current environment ## Environment Information - **vLLM version**: 0.9.2rc2.dev125+g49e8c7ea2.d20250710 - **PyTorch version**: torch2.7.0+cuda118 - **Transformers version**: 4.51.1 - **Model**: Qwen2Audio-7B-instruct - **OS**: Linux 4.18.0-425.3.1.el8.x86_64 - **GPU**: CUDA-enabled ``` ### 🐛 Describe the bug When using vLLM to serve Qwen2Audio-7B-instruct model, audio input requests result in 500 Internal Server Error, while text-only requests work fine. ## Steps to Reproduce ### 1. Start vLLM Server ```bash vllm serve /mnt/afs/share/Qwen2-Audio-7B-instruct \ --port 8006 \ --trust-remote-code \ --enforce-eager \ --max-model-len 8192 ``` ### 2. Test Text-Only Request (Works) ```bash curl -X POST "http://localhost:8006/v1/chat/completions" \ -H "Content-Type: application/json" \ -d '{ "model": "/mnt/afs/share/Qwen2-Audio-7B-instruct", "messages": [{"role": "user", "content": "Hello"}], "max_tokens": 100 }' ``` ### 3. Test Audio Request (Fails with 500 Internal Server Error) ``` with open("test.wav", "rb") as f: audio = f.read() audio_base64 = base64.b64encode(audio).decode("utf-8") openai_api_key = "EMPTY" openai_api_base = "http://localhost:8006/v1" client = OpenAI( api_ke...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen2Audio 500 internal Error bug;stale ### Your current environment ## Environment Information - **vLLM version**: 0.9.2rc2.dev125+g49e8c7ea2.d20250710 - **PyTorch version**: torch2.7.0+cuda118 - **Transformers...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Qwen2Audio 500 internal Error bug;stale ### Your current environment ## Environment Information - **vLLM version**: 0.9.2rc2.dev125+g49e8c7ea2.d20250710 - **PyTorch version**: torch2.7.0+cuda118 - **Transformers...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : 0.9.2rc2.dev125+g49e8c7ea2.d20250710 - **PyTorch version**: torch2.7.0+cuda118 - **Transformers version**: 4.51.1 - **Model**: Qwen2Audio-7B-instruct - **OS**: Linux 4.18.0-425.3.1.el8.x86_64 - **GPU**: CUDA-enabled `...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: Internal Server Error, while text-only requests work fine. ## Steps to Reproduce ### 1. Start vLLM Server ```bash vllm serve /mnt/afs/share/Qwen2-Audio-7B-instruct \ --port 8006 \ --trust-remote-code \ --enforce-eager \...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: stale ### Your current environment ## Environment Information - **vLLM version**: 0.9.2rc2.dev125+g49e8c7ea2.d20250710 - **PyTorch version**: torch2.7.0+cuda118 - **Transformers version**: 4.51.1 - **Model**: Qwen2Audio...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

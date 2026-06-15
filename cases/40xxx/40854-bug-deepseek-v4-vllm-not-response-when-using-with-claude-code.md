# vllm-project/vllm#40854: [Bug]: Deepseek V4 vllm not response when using with claude code

| 字段 | 值 |
| --- | --- |
| Issue | [#40854](https://github.com/vllm-project/vllm/issues/40854) |
| 状态 | open |
| 标签 | bug;DSv4 |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Deepseek V4 vllm not response when using with claude code

### Issue 正文摘录

### Your current environment docker run --gpus all \ --privileged --ipc=host -p 8077:8000 \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /data/models:/data/models \ -e VLLM_ENGINE_READY_TIMEOUT_S=3600 \ vllm/vllm-openai:deepseekv4-cu130 /data/models/DeepseekV4-pro \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 8 \ --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["all"]}' \ --attention_config.use_fp4_indexer_cache=True \ --tokenizer-mode deepseek_v4 \ --tool-call-parser deepseek_v4 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v4 \ --speculative_config '{"method":"mtp","num_speculative_tokens":2}' ### 🐛 Describe the bug Send request reply is OK , but when using claude code is very slow and even not response , other model didn't have this issue . ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: cu130 /data/models/DeepseekV4-pro \ --trust-remote-code \ --kv-cache-dtype fp8 \ --block-size 256 \ --enable-expert-parallel \ --data-parallel-size 8 \ --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "cust...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: run --gpus all \ --privileged --ipc=host -p 8077:8000 \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /data/models:/data/models \ -e VLLM_ENGINE_READY_TIMEOUT_S=3600 \ vllm/vllm-openai:deepseekv4-cu130 /data/mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e-expert-parallel \ --data-parallel-size 8 \ --compilation-config '{"cudagraph_mode":"FULL_AND_PIECEWISE", "custom_ops":["all"]}' \ --attention_config.use_fp4_indexer_cache=True \ --tokenizer-mode deepseek_v4 \ --tool-c...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 4 \ --enable-auto-tool-choice \ --reasoning-parser deepseek_v4 \ --speculative_config '{"method":"mtp","num_speculative_tokens":2}' ### 🐛 Describe the bug Send request reply is OK , but when using claude code is very sl...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: sponse when using with claude code bug;DSv4 ### Your current environment docker run --gpus all \ --privileged --ipc=host -p 8077:8000 \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -v /data/models:/data/models \ -...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

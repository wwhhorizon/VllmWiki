# vllm-project/vllm#29026: [Bug]: VLLM 0.11.1 Fails to recognize --rope-scaling arguement

| 字段 | 值 |
| --- | --- |
| Issue | [#29026](https://github.com/vllm-project/vllm/issues/29026) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: VLLM 0.11.1 Fails to recognize --rope-scaling arguement

### Issue 正文摘录

### Your current environment Running vllm 0.11.1 through docker. ### 🐛 Describe the bug The --rope-scaling argument used to enable long-context RoPE/YaRN scaling is available and functional in vLLM 0.11.0, but is missing in vLLM 0.11.1. In 0.11.1, the flag is rejected by the CLI and does not appear in vllm serve --help, preventing long-context configurations (e.g., for Qwen3 models). This appears to be a regression introduced between version 0.11.0 → 0.11.1. This is a regression affecting anyone attempting to use advanced RoPE/YaRN scaling settings in the CLI. Running: ``` vllm serve Qwen/Qwen3-4B-Instruct-2507 \ --download-dir /opt/hf_cache \ --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}' \ --port 8000 \ --dtype auto \ --max-model-len 70000 ``` Produces: ``` vllm: error: unrecognized arguments: --rope-scaling {"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768} ``` Similarly `vllm serve --help | grep rope` returns no results in 0.11.1, while it does display the parameter in 0.11.0. Actual Behavior • The CLI argument parser in vLLM 0.11.1 does not recognize --rope-scaling. • The flag is missing from help output and...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: he CLI and does not appear in vllm serve --help, preventing long-context configurations (e.g., for Qwen3 models). This appears to be a regression introduced between version 0.11.0 → 0.11.1. This is a regression affectin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g arguement bug ### Your current environment Running vllm 0.11.1 through docker. ### 🐛 Describe the bug The --rope-scaling argument used to enable long-context RoPE/YaRN scaling is available and functional in vLLM 0.11....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: g-context configurations (e.g., for Qwen3 models). This appears to be a regression introduced between version 0.11.0 → 0.11.1. This is a regression affecting anyone attempting to use advanced RoPE/YaRN scaling settings...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: or":4.0,"original_max_position_embeddings":32768}' \ --port 8000 \ --dtype auto \ --max-model-len 70000 ``` Produces: ``` vllm: error: unrecognized arguments: --rope-scaling {"rope_type":"yarn","factor":4.0,"original_ma...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .0. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

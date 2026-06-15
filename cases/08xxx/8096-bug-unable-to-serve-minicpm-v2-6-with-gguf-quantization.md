# vllm-project/vllm#8096: [Bug]: Unable to serve minicpm-v2.6 with GGUF quantization

| 字段 | 值 |
| --- | --- |
| Issue | [#8096](https://github.com/vllm-project/vllm/issues/8096) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Unable to serve minicpm-v2.6 with GGUF quantization

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug deploy minicpm-v-2.6model which download from [openbmb/MiniCPM-V-2_6-gguf](https://huggingface.co/openbmb/MiniCPM-V-2_6-gguf) by `vllm serve` ``` vllm serve models/minicpm/ggml-model-Q5_K_M.gguf --quantization gguf --kv-cache-dtype auto ``` get `AssertionError` in `weight_loader`: ``` File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py", line 1038, in load_model model.load_weights( File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen2.py", line 437, in load_weights weight_loader(param, loaded_weight) File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/layers/vocab_parallel_embedding.py", line 375, in weight_loader assert loaded_weight.shape[output_dim] == self.org_vocab_size AssertionError ERROR 09-03 11:29:27 api_server.py:171] RPCServer process died before responding to readiness probe ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: our current environment ### 🐛 Describe the bug deploy minicpm-v-2.6model which download from [openbmb/MiniCPM-V-2_6-gguf](https://huggingface.co/openbmb/MiniCPM-V-2_6-gguf) by `vllm serve` ``` vllm serve models/minicpm/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: Unable to serve minicpm-v2.6 with GGUF quantization bug ### Your current environment ### 🐛 Describe the bug deploy minicpm-v-2.6model which download from [openbmb/MiniCPM-V-2_6-gguf](https://huggingface.co/openbm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: vllm serve models/minicpm/ggml-model-Q5_K_M.gguf --quantization gguf --kv-cache-dtype auto ``` get `AssertionError` in `weight_loader`: ``` File "/home/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

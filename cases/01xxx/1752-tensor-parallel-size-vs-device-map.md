# vllm-project/vllm#1752: --tensor-parallel-size vs device_map?

| 字段 | 值 |
| --- | --- |
| Issue | [#1752](https://github.com/vllm-project/vllm/issues/1752) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> --tensor-parallel-size vs device_map?

### Issue 正文摘录

I have two 32G V100 gpus, and need to run a 13B float16 model. I have tried below paths: 1. python -m vllm.entrypoints.openai.api_server --dtype float16 --trust-remote-code --model /app/model --port 8000 --host 0.0.0.0 **--tensor-parallel-size 1**, OOM 2. python -m vllm.entrypoints.openai.api_server --dtype float16 --trust-remote-code --model /app/model --port 8000 --host 0.0.0.0 **--tensor-parallel-size 2**, both GPU usage is about 27G and can inference very fast with long tokens 3. use fastchat to start with 1 GPU,the GPU usage is about 27G, **The inference speed is fast but will stuck on long tokens.** 4. use fastchat to start with 2 GPUs, both GPU usage is about 14G, it use the device_map. **The inference speed is too slow with long tokens but won't stuck.** Questions: 1. Why --tensor-parallel-size 1 will cause OOM, the 1 GPU resource should be enough. 2. Does vllm support device_map? If there are only two 24G GPUs，how can I run such model with vllm? 3. How to speed up the inference when use device_map? (Maybe not specific with vllm, for discussion)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llel-size vs device_map? I have two 32G V100 gpus, and need to run a 13B float16 model. I have tried below paths: 1. python -m vllm.entrypoints.openai.api_server --dtype float16 --trust-remote-code --model /app/model --...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: m? 3. How to speed up the inference when use device_map? (Maybe not specific with vllm, for discussion)
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: del /app/model --port 8000 --host 0.0.0.0 **--tensor-parallel-size 1**, OOM 2. python -m vllm.entrypoints.openai.api_server --dtype float16 --trust-remote-code --model /app/model --port 8000 --host 0.0.0.0 **--tensor-pa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e vs device_map? I have two 32G V100 gpus, and need to run a 13B float16 model. I have tried below paths: 1. python -m vllm.entrypoints.openai.api_server --dtype float16 --trust-remote-code --model /app/model --port 800...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#32125: [Bug]: GPTOSS Reasoning Content split is not perfect in vllm/vllm-openai:v0.13.0 and nightly build

| 字段 | 值 |
| --- | --- |
| Issue | [#32125](https://github.com/vllm-project/vllm/issues/32125) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPTOSS Reasoning Content split is not perfect in vllm/vllm-openai:v0.13.0 and nightly build

### Issue 正文摘录

### Your current environment ``` docker run -d --security-opt apparmor=unconfined \ --name gptoss20b \ --restart unless-stopped \ --gpus '"device=0,3"' \ -p 9004:9000 \ -v /mnt/aidisk/cache:/root/.cache \ -v /home/debian/vllm_serve/GPT-OSS_Blackwell.yaml:/root/GPT-OSS_Blackwell.yaml \ -e VLLM_SLEEP_WHEN_IDLE=1 \ -e HF_HUB_OFFLINE=1 \ -e TRANSFORMERS_OFFLINE=1 \ -e TIKTOKEN_ENCODINGS_BASE=/root/.cache/tiktoken_encodings \ vllm/vllm-openai:v0.13.0 \ --model openai/gpt-oss-20b \ --config /root/GPT-OSS_Blackwell.yaml \ --reasoning-parser openai_gptoss \ -tp 2 --gpu-memory-utilization 0.80 \ --port 9000 --swap-space 0 ``` GPT-OSS_Blackwell.yaml: ``` kv-cache-dtype: fp8 compilation-config: '{"pass_config":{"fuse_allreduce_rms":true,"eliminate_noops":true}}' async-scheduling: true no-enable-prefix-caching: true max-cudagraph-capture-size: 2048 max-num-batched-tokens: 8192 stream-interval: 20 ``` ### 🐛 Describe the bug Streaming Response - reasoning_content in 2nd should be "plus surname. But question ambiguous." but currently it is null and text is moved to content. ``` data: {"id":"chatcmpl-b8a21b970ab11bfb","object":"chat.completion.chunk","created":1768147682,"model":"openai/gpt-oss-2...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 04:9000 \ -v /mnt/aidisk/cache:/root/.cache \ -v /home/debian/vllm_serve/GPT-OSS_Blackwell.yaml:/root/GPT-OSS_Blackwell.yaml \ -e VLLM_SLEEP_WHEN_IDLE=1 \ -e HF_HUB_OFFLINE=1 \ -e TRANSFORMERS_OFFLINE=1 \ -e TIKTOKEN_EN...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: \ -v /mnt/aidisk/cache:/root/.cache \ -v /home/debian/vllm_serve/GPT-OSS_Blackwell.yaml:/root/GPT-OSS_Blackwell.yaml \ -e VLLM_SLEEP_WHEN_IDLE=1 \ -e HF_HUB_OFFLINE=1 \ -e TRANSFORMERS_OFFLINE=1 \ -e TIKTOKEN_ENCODINGS_...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ing Content split is not perfect in vllm/vllm-openai:v0.13.0 and nightly build bug ### Your current environment ``` docker run -d --security-opt apparmor=unconfined \ --name gptoss20b \ --restart unless-stopped \ --gpus...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: \ --port 9000 --swap-space 0 ``` GPT-OSS_Blackwell.yaml: ``` kv-cache-dtype: fp8 compilation-config: '{"pass_config":{"fuse_allreduce_rms":true,"eliminate_noops":true}}' async-scheduling: true no-enable-prefix-caching:...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: tion 0.80 \ --port 9000 --swap-space 0 ``` GPT-OSS_Blackwell.yaml: ``` kv-cache-dtype: fp8 compilation-config: '{"pass_config":{"fuse_allreduce_rms":true,"eliminate_noops":true}}' async-scheduling: true no-enable-prefix...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

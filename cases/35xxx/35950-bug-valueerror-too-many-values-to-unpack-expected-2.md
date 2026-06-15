# vllm-project/vllm#35950: [Bug]: ValueError: too many values to unpack (expected 2)

| 字段 | 值 |
| --- | --- |
| Issue | [#35950](https://github.com/vllm-project/vllm/issues/35950) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: too many values to unpack (expected 2)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (vllm-m4) wendell@Wendell-Mac Qwen3.5-2B % python -m vllm.entrypoints.openai.api_server \ --model . \ --served-model-name Qwen3.5-2B \ --dtype auto \ --trust-remote-code \ --host 0.0.0.0 \ --port 8000 \ --max-model-len 16384 \ --enforce-eager \ --disable-custom-all-reduce \ --kv-cache-dtype auto objc[28103]: Class AVFFrameReceiver is implemented in both /opt/anaconda3/envs/vllm-m4/lib/python3.11/site-packages/av/.dylibs/libavdevice.62.1.100.dylib (0x11c5ec3a8) and /opt/anaconda3/envs/vllm-m4/lib/python3.11/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x12ff9c3a8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed. objc[28103]: Class AVFAudioReceiver is implemented in both /opt/anaconda3/envs/vllm-m4/lib/python3.11/site-packages/av/.dylibs/libavdevice.62.1.100.dylib (0x11c5ec3f8) and /opt/anaconda3/envs/vllm-m4/lib/python3.11/site-packages/cv2/.dylibs/libavdevice.61.3.100.dylib (0x12ff9c3f8). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed. INFO 03-04 11:33:47 [importing.py:68] Triton not insta...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: . One of the duplicates must be removed or renamed. INFO 03-04 11:33:47 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. (APIServer pid=28103) INFO 03-04 11:...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: openai.api_server \ --model . \ --served-model-name Qwen3.5-2B \ --dtype auto \ --trust-remote-code \ --host 0.0.0.0 \ --port 8000 \ --max-model-len 16384 \ --enforce-eager \ --disable-custom-all-reduce \ --kv-cache-dty...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nt environment ### 🐛 Describe the bug (vllm-m4) wendell@Wendell-Mac Qwen3.5-2B % python -m vllm.entrypoints.openai.api_server \ --model . \ --served-model-name Qwen3.5-2B \ --dtype auto \ --trust-remote-code \ --host 0....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: icates must be removed or renamed. INFO 03-04 11:33:47 [importing.py:68] Triton not installed or not compatible; certain GPU-related functions will not be available. (APIServer pid=28103) INFO 03-04 11:33:49 [utils.py:3...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: odel-len 16384 \ --enforce-eager \ --disable-custom-all-reduce \ --kv-cache-dtype auto objc[28103]: Class AVFFrameReceiver is implemented in both /opt/anaconda3/envs/vllm-m4/lib/python3.11/site-packages/av/.dylibs/libav...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

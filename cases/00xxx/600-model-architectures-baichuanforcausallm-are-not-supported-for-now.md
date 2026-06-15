# vllm-project/vllm#600: Model architectures ['BaichuanForCausalLM'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#600](https://github.com/vllm-project/vllm/issues/600) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Model architectures ['BaichuanForCausalLM'] are not supported for now.

### Issue 正文摘录

```python INFO 07-27 17:20:09 llm_engine.py:67] Initializing an LLM engine with config: model='./baichuan-inc--Baichuan-13B-Chat/snapshots/d0a98e13222c6e82d24062f60ff491519e249744', tokenizer='./baichuan-inc--Baichuan-13B-Chat/snapshots/d0a98e13222c6e82d24062f60ff491519e249744', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) WARNING 07-27 17:20:09 tokenizer.py:63] Using a slow tokenizer. This might cause a significant slowdown. Consider using a fast tokenizer instead. ts-253610bc360a49f2b5909ce950baf8d2-launcher:13189:13189 [0] NCCL INFO NET/Plugin : No plugin found (libnccl-net.so), using internal implementation ts-253610bc360a49f2b5909ce950baf8d2-launcher:13189:13189 [0] NCCL INFO cudaDriverVersion 11000 NCCL version 2.14.3+cuda11.7 ts-253610bc360a49f2b5909ce950baf8d2-launcher:13189:13268 [0] NCCL INFO Using network IB ts-253610bc360a49f2b5909ce950baf8d2-launcher:13189:13268 [0] NCCL INFO Setting affinity for GPU 0 to e3,80080000,00e38000 ts-253610bc360a49f2b5909ce950baf8d2-launcher:13189:13268 [0] NCCL INFO Channel 00/32 : 0 ts-253610bc360a49f2b5909ce950baf8d2-la...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Model architectures ['BaichuanForCausalLM'] are not supported for now. ```python INFO 07-27 17:20:09 llm_engine.py:67] Initializing an LLM engine with config: model='./baichuan-inc--Baichuan-13B-Chat/snapshots/d0a98e1322
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 2d24062f60ff491519e249744', tokenizer_mode=auto, trust_remote_code=True, dtype=torch.float16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=1, seed=0) WARNING 07-27 17:20:09 toke...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: Model architectures ['BaichuanForCausalLM'] are not supported for now. ```python INFO 07-27 17:20:09 llm_engine.py:67] Initializing an LLM engine with config: model='./baichuan-inc--Baichuan-13B-Chat/snapshots/d0a98e132...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 0bc360a49f2b5909ce950baf8d2-launcher:13189:13189 [0] NCCL INFO cudaDriverVersion 11000 NCCL version 2.14.3+cuda11.7 ts-253610bc360a49f2b5909ce950baf8d2-launcher:13189:13268 [0] NCCL INFO Using network IB ts-253610bc360a...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: t supported for now. Supported architectures: ['BaiChuanForCausalLM', 'BloomForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MPT...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

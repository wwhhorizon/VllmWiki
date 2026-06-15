# vllm-project/vllm#1700: Run long conetxt error : CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#1700](https://github.com/vllm-project/vllm/issues/1700) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | cuda;kernel;operator;sampling |
| 症状 | build_error;crash;mismatch;oom |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> Run long conetxt error : CUDA error: an illegal memory access was encountered

### Issue 正文摘录

**prompt len: 6495, max_tokens: 21000** **running command :** `python benchmark_serving.py --backend=vllm --host=localhost --port=8888 --dataset=/mnt/vllm/benchmarks/fake_data --tokenizer=/mnt/disk2/lama-tokenizer --num-prompts=1 ` `python -m vllm.entrypoints.api_server --model=/mnt/disk2/llama-2-13b-chat-hf/ --tokenizer=/mnt/disk2/lama-tokenizer --tensor-parallel-size=2 --swap-space=64 --engine-use-ray --worker-use-ray --max-num-batched-tokens=60000` ``` INFO 11-17 08:58:33 async_llm_engine.py:371] Received request 93296c1db0b24cfbb2ee20b7208ceced: prompt: ' U1XiBoEelEJeEDfIAGLrf27N9d1********dgbZq8fXYw215vKF2k77Cjb', sampling params: SamplingParams(n=1, best_of=1, presence_penalty=0.0, frequency_penalty=0.0, repetition_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=True, max_tokens=21000, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True), prompt token ids: None. Error log: (RayWorker pid=296668) [2023-11-17 08:38:23,099 E 296668 296668] logging.cc:97: Unhandled exception: N3c105ErrorE. what(): CUDA error: an illegal memory access was encounter...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: max_tokens: 21000** **running command :** `python benchmark_serving.py --backend=vllm --host=localhost --port=8888 --dataset=/mnt/vllm/benchmarks/fake_data --tokenizer=/mnt/disk2/lama-tokenizer --num-prompts=1 ` `python...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: os=True, max_tokens=21000, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True), prompt token ids: None. Error log: (RayWorker pid=296668) [2023-11-17 08:38:23,099 E 296668...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: -tokenizer --num-prompts=1 ` `python -m vllm.entrypoints.api_server --model=/mnt/disk2/llama-2-13b-chat-hf/ --tokenizer=/mnt/disk2/lama-tokenizer --tensor-parallel-size=2 --swap-space=64 --engine-use-ray --worker-use-ra...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Run long conetxt error : CUDA error: an illegal memory access was encountered **prompt len: 6495, max_tokens: 21000** **running command :** `python benchmark_serving.py --backend=vllm --host=localhost --port=8888 --data...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: on_penalty=1.0, temperature=1.0, top_p=1.0, top_k=-1, use_beam_search=False, length_penalty=1.0, early_stopping=False, stop=[], ignore_eos=True, max_tokens=21000, logprobs=None, prompt_logprobs=None, skip_special_tokens...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | dist-packages/torch/lib/libc10_cuda.so) (rayworker pid=296668) frame #4: <unknown function> + 0x2b930 (0x7f5ab071b930 in /usr/local/lib/python3.8/dist-packages/torch/lib/libc10_cu… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | -packages/torch/lib/libtorch_python.so) (rayworker pid=296668) frame #6: <unknown function> + 0x3ee77 (0x7f5ab8073e77 in /usr/local/lib/python3.8/dist-packages/torch/lib/libc10.so) |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | n3.8/dist-packages/torch/lib/libc10.so) (rayworker pid=296668) frame #7: c10::tensorimpl::~tensorimpl() + 0x1be (0x7f5ab806c69e in /usr/local/lib/python3.8/dist-packages/torch/lib… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | ::rayworker.execute_method() [0x5ecd90] (rayworker pid=296668) frame #12: ray::rayworker.execute_method() [0x5447b8] (rayworker pid=296668) frame #13: ray::rayworker.execute_metho… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | ::rayworker.execute_method() [0x54480a] (rayworker pid=296668) frame #16: ray::rayworker.execute_method() [0x54480a] (rayworker pid=296668) frame #17: ray::rayworker.execute_metho… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | ::rayworker.execute_method() [0x54480a] (rayworker pid=296668) frame #20: ray::rayworker.execute_method() [0x54480a] (rayworker pid=296668) frame #21: ray::rayworker.execute_metho… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | ::rayworker.execute_method() [0x54480a] (rayworker pid=296668) frame #21: ray::rayworker.execute_method() [0x54480a] (rayworker pid=296668) frame #22: ray::rayworker.execute_metho… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | python3.8/dist-packages/ray/_raylet.so) (rayworker pid=296668) frame #27: ray::core::coreworker::executetask(ray::taskspecification const&, std::shared_ptr<std::unordered_map<std:… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | python3.8/dist-packages/ray/_raylet.so) (rayworker pid=296668) frame #29: <unknown function> + 0x793684 (0x7f5abd005684 in /usr/local/lib/python3.8/dist-packages/ray/_raylet.so) (… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | python3.8/dist-packages/ray/_raylet.so) (rayworker pid=296668) frame #32: ray::core::actorschedulingqueue::acceptrequestorrejectifcanceled(ray::taskid, ray::core::inboundrequest&)… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | 8e267 in ray::rayworker.execute_method) (rayworker pid=296668) frame #53: ray::rayworker.execute_method() [0x67d9b1] (rayworker pid=296668) frame #54: ray::rayworker.execute_metho… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

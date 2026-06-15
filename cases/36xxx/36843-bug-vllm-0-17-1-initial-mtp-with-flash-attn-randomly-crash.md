# vllm-project/vllm#36843: [Bug]: VLLM 0.17.1 initial mtp with FLASH_ATTN randomly crash

| 字段 | 值 |
| --- | --- |
| Issue | [#36843](https://github.com/vllm-project/vllm/issues/36843) |
| 状态 | open |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: VLLM 0.17.1 initial mtp with FLASH_ATTN randomly crash

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when execute VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=1 vllm serve Qwen/Qwen3.5-27B-GPTQ-Int4 --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":5}' -tp 2 , it randomly crash with error msg:(Worker pid=1377089) (Worker_TP0 pid=1377089) ERROR 03-12 11:38:40 [multiproc_executor.py:932] self.module, self.function, self.n_regs, self.n_spills, self.n_max_threads = driver.active.utils.load_binary( (Worker pid=1377089) (Worker_TP0 pid=1377089) ERROR 03-12 11:38:40 [multiproc_executor.py:932] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker pid=1377089) (Worker_TP0 pid=1377089) ERROR 03-12 11:38:40 [multiproc_executor.py:932] RuntimeError: Triton Error [CUDA]: operation not permitted when stream is capturing full error msg: ``` VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=1 vllm serve Qwen/Qwen3.5-27B-GPTQ-Int4 --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":5}' -tp 2 (APIServer pid=1375776) INFO 03-12 11:36:49 [utils.py:297] (APIServer pid=1375776) INFO 03-12 11:36:49 [utils.py:297] █ █ █▄ ▄█ (APIServer pid=1375776) INFO 03-12 11:36:49 [utils.py:297] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.1rc1.dev83+g8647c6c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: bug when execute VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=1 vllm serve Qwen/Qwen3.5-27B-GPTQ-Int4 --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":5}' -tp 2 , it randomly crash with error msg:(W...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: =1377089) ERROR 03-12 11:38:40 [multiproc_executor.py:932] RuntimeError: Triton Error [CUDA]: operation not permitted when stream is capturing full error msg: ``` VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=1 vllm serve Qw...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: =1375776) INFO 03-12 11:36:49 [utils.py:297] ▄▄ ▄█ █ █ █ ▀▄▀ █ version 0.17.1rc1.dev83+g8647c6cf5 (APIServer pid=1375776) INFO 03-12 11:36:49 [utils.py:297] █▄█▀ █ █ █ █ model Qwen/Qwen3.5-27B-GPTQ-Int4 (APIServer pid=1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: ### 🐛 Describe the bug when execute VLLM_MEMORY_PROFILER_ESTIMATE_CUDAGRAPHS=1 vllm serve Qwen/Qwen3.5-27B-GPTQ-Int4 --speculative-config '{"method":"qwen3_next_mtp","num_speculative_tokens":5}' -tp 2 , it randomly cras...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 5: erver pid=1375776) INFO 03-12 11:36:52 [config.py:224] Setting attention block size to 816 tokens to ensure that attention page size is >= mamba page size. (APIServer pid=1375776) INFO 03-12 11:36:52 [config.py:255] Pad...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

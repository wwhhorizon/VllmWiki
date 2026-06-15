# vllm-project/vllm#11168: [Bug]: vllm.core.block.interfaces.BlockAllocator.NoFreeBlocksError to old Mistral Model

| 字段 | 值 |
| --- | --- |
| Issue | [#11168](https://github.com/vllm-project/vllm/issues/11168) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;attention_kv_cache;ci_build;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | activation;cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm.core.block.interfaces.BlockAllocator.NoFreeBlocksError to old Mistral Model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is what is logged from `vllm serve` ``` ERROR 12-13 08:58:11 engine.py:165] NoFreeBlocksError() ERROR 12-13 08:58:11 engine.py:165] Traceback (most recent call last): ERROR 12-13 08:58:11 engine.py:165] File "/workspace-lib/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 163, in start ERROR 12-13 08:58:11 engine.py:165] self.run_engine_loop() ERROR 12-13 08:58:11 engine.py:165] File "/workspace-lib/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 226, in run_engine_loop ERROR 12-13 08:58:11 engine.py:165] request_outputs = self.engine_step() ERROR 12-13 08:58:11 engine.py:165] ^^^^^^^^^^^^^^^^^^ ERROR 12-13 08:58:11 engine.py:165] File "/workspace-lib/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 244, in engine_step ERROR 12-13 08:58:11 engine.py:165] raise e ERROR 12-13 08:58:11 engine.py:165] File "/workspace-lib/lib/python3.11/site-packages/vllm/engine/multiprocessing/engine.py", line 235, in engine_step ERROR 12-13 08:58:11 engine.py:165] return self.engine.step() ERROR 12-13 08:58:11 engine.py:165] ^^^^^^^^...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: ock.interfaces.BlockAllocator.NoFreeBlocksError to old Mistral Model bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is what is logged from `vllm serve` ``` ERROR 1...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.36.2", "use_cache": true, "vocab_size": 32019 } ``` I suspect there is problem because of the model. I'm using mistral as base model. Her...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 00.0, "sliding_window": 4096, "tie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.36.2", "use_cache": true, "vocab_size": 32019 } ``` I suspect there is problem because of the model. I'm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: [Bug]: vllm.core.block.interfaces.BlockAllocator.NoFreeBlocksError to old Mistral Model bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is what is logged from `vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: file of the model I serve ```json { "_name_or_path": "mistral-7B", "architectures": [ "MistralForCausalLM" ], "attention_dropout": 0.0, "bos_token_id": 1, "eos_token_id": 32000, "hidden_act": "silu", "hidden_size": 4096...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

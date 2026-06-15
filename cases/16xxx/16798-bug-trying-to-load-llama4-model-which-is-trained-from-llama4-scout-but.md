# vllm-project/vllm#16798: [Bug]: Trying to load llama4 model which is trained from llama4 scout. But this is text only fine tune and has the following config.

| 字段 | 值 |
| --- | --- |
| Issue | [#16798](https://github.com/vllm-project/vllm/issues/16798) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Trying to load llama4 model which is trained from llama4 scout. But this is text only fine tune and has the following config.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Issue's stack trace is : ```text 267718) INFO 04-17 18:03:55 [gpu_model_runner.py:1276] Starting to load model /mnt/llama_ft/pytorch_model_folder... Line 11: (VllmWorker rank=3 pid=267718) INFO 04-17 18:03:55 [transformers.py:118] Using Transformers backend. Line 20: (VllmWorker rank=3 pid=267718) Process SpawnProcess-1:4: Line 23: (VllmWorker rank=3 pid=267718) Traceback (most recent call last): Line 26: (VllmWorker rank=3 pid=267718) File "/home/azureuser/miniconda3/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap Line 28: (VllmWorker rank=3 pid=267718) self.run() Line 30: (VllmWorker rank=3 pid=267718) File "/home/azureuser/miniconda3/lib/python3.12/multiprocessing/process.py", line 108, in run Line 32: (VllmWorker rank=3 pid=267718) self._target(*self._args, **self._kwargs) Line 33: (VllmWorker rank=3 pid=267718) File "/home/azureuser/miniconda3/lib/python3.12/site-packages/vllm/v1/executor/multiproc_executor.py", line 316, in worker_main Line 35: (VllmWorker rank=3 pid=267718) worker = WorkerProc(*args, **kwargs) Line 37: (VllmWorker rank=3 pid=267718) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ Line 39: (VllmWorker rank=...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ie_word_embeddings": false, "torch_dtype": "bfloat16", "transformers_version": "4.51.3", "use_cache": false, "use_qk_norm": true, "vocab_size": 201136 }. This error gets solved if there is AutoModelForCausalLM instead o...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: lse, "attention_chunk_size": 8192, "attention_dropout": 0.0, "attn_scale": 0.1, "attn_temperature_tuning": 4, "bos_token_id": 200000, "cache_implementation": "hybrid", "eos_token_id": [ 200001, 200007, 200008 ], "floor_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Trying to load llama4 model which is trained from llama4 scout. But this is text only fine tune and has the following config. bug;stale ### Your current environment ### 🐛 Describe the bug Issue's stack trace is :...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t__ Line 76: (VllmWorker rank=3 pid=267718) self.model = TransformersModel(vllm_config=vllm_config, prefix=prefix) Line 78: (VllmWorker rank=3 pid=267718) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Line 8...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: silu", "hidden_size": 5120, "initializer_range": 0.02, "interleave_moe_layer_step": 1, "intermediate_size": 8192, "intermediate_size_mlp": 16384, "max_position_embeddings": 10485760, "model_type": "llama4_text", "moe_la...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

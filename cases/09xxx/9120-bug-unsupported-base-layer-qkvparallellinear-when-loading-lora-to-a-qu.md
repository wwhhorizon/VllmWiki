# vllm-project/vllm#9120: [Bug]: Unsupported base layer: QKVParallelLinear when loading lora to a quantized model

| 字段 | 值 |
| --- | --- |
| Issue | [#9120](https://github.com/vllm-project/vllm/issues/9120) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | activation;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unsupported base layer: QKVParallelLinear when loading lora to a quantized model

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is how I load my model using vllm serve ```bash vllm serve --host 0.0.0.0 --served-model-name my-model --port 8000 --enable-lora --lora-modules my-model:lora= ``` And here is the error that I got ```python Process SpawnProcess-1: Traceback (most recent call last): File "/home/fahadh/anaconda3/envs/vllm/lib/python3.11/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/home/fahadh/anaconda3/envs/vllm/lib/python3.11/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/fahadh/vllm/vllm/engine/multiprocessing/engine.py", line 388, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/fahadh/vllm/vllm/engine/multiprocessing/engine.py", line 138, in from_engine_args return cls( ^^^^ File "/home/fahadh/vllm/vllm/engine/multiprocessing/engine.py", line 78, in __init__ self.engine = LLMEngine(*args, ^^^^^^^^^^^^^^^^ File "/home/fahadh/vllm/vllm/engine/llm_engine.py", line 338, in __init__ self.model_executor = executor_class( ^^^^^^^^^^^^^^^ F...

## 现有链接修复摘要

#9179 [Bugfix] Fix lora loading for Compressed Tensors in #9120

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ^^^^^^^^^^^^ File "/home/fahadh/anaconda3/envs/vllm/lib/python3.11/asyncio/runners.py", line 118, in run return self._loop.run_until_complete(task) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "uvloop/loop.pyx", line 1517,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Unsupported base layer: QKVParallelLinear when loading lora to a quantized model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is how I load my model using vllm...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: .py", line 457, in _create_lora_modules from_layer(module, self.lora_slots, self.lora_config, File "/home/fahadh/vllm/vllm/lora/utils.py", line 64, in from_layer ret = lora_cls(layer) ^^^^^^^^^^^^^^^ File "/home/fahadh/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: supported base layer: QKVParallelLinear when loading lora to a quantized model bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Here is how I load my model using vllm serve ```...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ^ File "/home/fahadh/vllm/vllm/scripts.py", line 191, in main args.dispatch_function(args) File "/home/fahadh/vllm/vllm/scripts.py", line 40, in serve uvloop.run(run_server(args)) File "/home/fahadh/anaconda3/envs/vllm/...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9179](https://github.com/vllm-project/vllm/pull/9179) | closes_keyword | 0.95 | [Bugfix] Fix lora loading for Compressed Tensors in #9120 | FIX #9120 (*link existing issues this PR will resolve*) **BEFORE SUBMITTING, PLEASE READ THE CHECKLIST BELOW AND FILL IN THE DESCRIPTION ABOVE** --- <details> <!-- inside |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

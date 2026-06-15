# vllm-project/vllm#31276: [Bug]: Stuck with a loop when tensor_parallel_size=2

| 字段 | 值 |
| --- | --- |
| Issue | [#31276](https://github.com/vllm-project/vllm/issues/31276) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Stuck with a loop when tensor_parallel_size=2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The following python code got stuck when tensor_parallel_size set to 2, with GPU-util = 100%, %CPU = 100% and MEM = 0%. However, when set to 4, it works fine. ```python from vllm import LLM, SamplingParams import os os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" import torch llm_instance_params_dict = { "dtype":"bfloat16", "tensor_parallel_size":2, # 4 "trust_remote_code":True, "gpu_memory_utilization":0.9 } sampling_params_dict = SamplingParams( max_tokens=1024, top_k=50, top_p=0.95, temperature=0.7, ) full_model_path_to_load = os.path.join("models", "gemma-3-27b-it") llm_instance = LLM(full_model_path_to_load, **llm_instance_params_dict) print(f"Loaded model {full_model_path_to_load}") outputs = llm_instance.generate(["Hello world"], sampling_params_dict) print(f"Test outputs {outputs}") ``` The KeyboardInterrupt traceback is as followed. ```python Traceback (most recent call last): File "/home/lky/vllm/occupation.py", line 23, in llm_instance = LLM(full_model_path_to_load, **llm_instance_params_dict) File "/home/lky/vllm/.venv/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 351, in __init__ self.llm_engine = LLMEng...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nd MEM = 0%. However, when set to 4, it works fine. ```python from vllm import LLM, SamplingParams import os os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" import torch llm_instance_params_dict = { "dtype":"bfloat16", "...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: DEVICES"] = "0,1,2,3" import torch llm_instance_params_dict = { "dtype":"bfloat16", "tensor_parallel_size":2, # 4 "trust_remote_code":True, "gpu_memory_utilization":0.9 } sampling_params_dict = SamplingParams( max_token...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: _tokens=1024, top_k=50, top_p=0.95, temperature=0.7, ) full_model_path_to_load = os.path.join("models", "gemma-3-27b-it") llm_instance = LLM(full_model_path_to_load, **llm_instance_params_dict) print(f"Loaded model {ful...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: , in poll return zmq_poll(self.sockets, timeout=timeout) File "zmq/backend/cython/_zmq.py", line 1680, in zmq.backend.cython._zmq.zmq_poll File "zmq/backend/cython/_zmq.py", line 179, in zmq.backend.cython._zmq._check_r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e. ```python from vllm import LLM, SamplingParams import os os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3" import torch llm_instance_params_dict = { "dtype":"bfloat16", "tensor_parallel_size":2, # 4 "trust_remote_code":...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#10085: [Bug]: fixie-ai/ultravox-v0_4 throws Out of Memory

| 字段 | 值 |
| --- | --- |
| Issue | [#10085](https://github.com/vllm-project/vllm/issues/10085) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: fixie-ai/ultravox-v0_4 throws Out of Memory

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I try to deploy the model, it throws OOM: ``` vllm serve fixie-ai/ultravox-v0_4 --tensor-parallel-size 2 --max-model-len 120000 --trust-remote-code ``` ``` (VllmWorkerProcess pid=35734) INFO 11-06 17:51:01 model_runner.py:1066] Loading model weights took 8.1626 GB INFO 11-06 17:51:01 model_runner.py:1066] Loading model weights took 8.1626 GB (VllmWorkerProcess pid=35734) /opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/nn/modules/linear.py:125: UserWarning: Attempting to use hipBLASLt on an unsupported architecture! Overriding blas backend to hipblas (Triggered internally at ../aten/src/ATen/Context.cpp:288.) (VllmWorkerProcess pid=35734) return F.linear(input, self.weight, self.bias) (VllmWorkerProcess pid=35734) INFO 11-06 17:51:06 model_runner_base.py:120] Writing input of failed execution to /tmp/err_execute_model_input_20241106-175106.pkl... /opt/conda/envs/py_3.9/lib/python3.9/site-packages/torch/nn/modules/linear.py:125: UserWarning: Attempting to use hipBLASLt on an unsupported architecture! Overriding blas backend to hipblas (Triggered internally at ../aten/src/ATen/Contex...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: empting to use hipBLASLt on an unsupported architecture! Overriding blas backend to hipblas (Triggered internally at ../aten/src/ATen/Context.cpp:288.) (VllmWorkerProcess pid=35734) return F.linear(input, self.weight, s...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: r: HIP out of memory. Tried to allocate 34.33 GiB. GPU 1 has a total capacity of 31.98 GiB of which 10.55 GiB is free. Of the allocated memory 20.23 GiB is allocated by PyTorch, and 784.37 MiB is reserved by PyTorch but...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -packages/torch/nn/modules/linear.py:125: UserWarning: Attempting to use hipBLASLt on an unsupported architecture! Overriding blas backend to hipblas (Triggered internally at ../aten/src/ATen/Context.cpp:288.) (VllmWork...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: fixie-ai/ultravox-v0_4 throws Out of Memory bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I try to deploy the model, it throws OOM: ``` vllm serve fixie-ai...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: worker VllmWorkerProcess while processing method determine_num_available_blocks. (VllmWorkerProcess pid=35734) ERROR 11-06 17:51:07 multiproc_worker_utils.py:229] Traceback (most recent call last): (VllmWorkerProcess pi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

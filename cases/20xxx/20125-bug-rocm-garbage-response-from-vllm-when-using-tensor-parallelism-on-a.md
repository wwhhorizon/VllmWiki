# vllm-project/vllm#20125: [Bug][Rocm] Garbage Response from vLLM When Using Tensor Parallelism on AMD CPX/NPS4 Partitioned GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#20125](https://github.com/vllm-project/vllm/issues/20125) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug][Rocm] Garbage Response from vLLM When Using Tensor Parallelism on AMD CPX/NPS4 Partitioned GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Steps to reproduce:** We referred to doc: [Steps to Run a vLLM Workload on AMD partition](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/gpu-partitioning/mi300x/run-vllm.html). - [ ] **Do CPS/NPS4 Partition** `sudo amd-smi set --memory-partition NPS4` - [ ] **Launch container** `docker run -it --network=host --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device /dev/kfd --device /dev/dri rocm/vllm:latest /bin/bash` - [ ] **Set Env** ``` export HF_TOKEN= export HIP_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 ``` - [ ] `vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 8` - [ ] **Query the model** ``` curl http://localhost:8000/v1/chat/completions \ -H 'Content-Type: application/json' \ --data '{ "model": "meta-llama/Llama-3.1-8B-Instruct", "messages": [ {"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is Deep Learning?"} ] }' ``` **Actual behaviour:** Garbled and nonsensical output as below {"id":"chatcmpl-5488b13e1910409d884196f041b34b0b","object":"chat.completion","created":1750923599,"model":"meta-llama/Llama-3.1-8B-Instr...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: [Bug][Rocm] Garbage Response from vLLM When Using Tensor Parallelism on AMD CPX/NPS4 Partitioned GPUs bug;rocm;stale ### Your current environment ### 🐛 Describe the bug **Steps to reproduce:** We referred to doc: [Steps
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vice /dev/dri rocm/vllm:latest /bin/bash` - [ ] **Set Env** ``` export HF_TOKEN= export HIP_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 ``` - [ ] `vllm serve meta-llama/Llama-3.1-8B-Instruct --tensor-parallel-size 8` - [ ] **Query...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: `sudo amd-smi set --memory-partition NPS4` - [ ] **Launch container** `docker run -it --network=host --group-add=video --ipc=host --cap-add=SYS_PTRACE --security-opt seccomp=unconfined --device /dev/kfd --device /dev/dr...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: tale ### Your current environment ### 🐛 Describe the bug **Steps to reproduce:** We referred to doc: [Steps to Run a vLLM Workload on AMD partition](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/gpu-parti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: n AMD partition](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/gpu-partitioning/mi300x/run-vllm.html). - [ ] **Do CPS/NPS4 Partition** `sudo amd-smi set --memory-partition NPS4` - [ ] **Launch container**...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

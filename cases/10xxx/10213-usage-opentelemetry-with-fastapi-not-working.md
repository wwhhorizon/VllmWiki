# vllm-project/vllm#10213: [Usage]: OpenTelemetry with fastapi not working

| 字段 | 值 |
| --- | --- |
| Issue | [#10213](https://github.com/vllm-project/vllm/issues/10213) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: OpenTelemetry with fastapi not working

### Issue 正文摘录

### Your current environment ```text ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.3.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: Could not collect NVIDIA_VISIBLE_DEVICES=all NVIDIA_REQUIRE_CUDA=cuda>=12.1 brand=tesla,driver>=470,driver =470,driver =470,driver =470,driver =470,driver =470,driver =470,driver =470,driver =470,driver =470,driver =525,driver =525,driver =525,driver =525,driver =525,driver =525,driver =525,driver =525,driver =525,driver =525,driver<526 NCCL_VERSION=2.17.1-1 NVIDIA_DRIVER_CAPABILITIES=compute,utility NVIDIA_PRODUCT_NAME=CUDA NVIDIA_CPU_ONLY=1 NVIDIA_CUDA_END_OF_LIFE=1 CUDA_VERSION=12.1.0 LD_LIBRARY_PATH=/usr/local/lib/python3.10/dist-packages/cv2/../../lib64:/usr/local/nvidia/lib:/usr/local/nvidia/lib64 ``` ### How would you like to use vllm I am running a fastapi of a llama model. Based on [vllm/examples/production_monitoring /Otel.md](https://github.com/vllm-project/vllm/blob/main/examples/production_monitoring/Otel.md) I am able to us `dummy_client.py`. As followed image ![image](https://github.com/user-attachments/assets/10c16251-1650-44fd-8d60-dc472e35b1d6) However, for the...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: stapi not working usage;stale ### Your current environment ```text ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.3.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disable...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: th fastapi not working usage;stale ### Your current environment ```text ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.3.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Di...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: b64 ``` ### How would you like to use vllm I am running a fastapi of a llama model. Based on [vllm/examples/production_monitoring /Otel.md](https://github.com/vllm-project/vllm/blob/main/examples/production_monitoring/O...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: OpenTelemetry with fastapi not working usage;stale ### Your current environment ```text ROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.6.3.post1 vLLM Build Flags: CUDA Archs: Not Set; R...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;hardware_porting;model_support cuda build_error env_dependency Y...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

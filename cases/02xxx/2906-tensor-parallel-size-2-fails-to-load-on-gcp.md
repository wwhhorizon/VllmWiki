# vllm-project/vllm#2906: --tensor-parallel-size 2 fails to load on GCP

| 字段 | 值 |
| --- | --- |
| Issue | [#2906](https://github.com/vllm-project/vllm/issues/2906) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> --tensor-parallel-size 2 fails to load on GCP

### Issue 正文摘录

Hi, I am trying to set up vLLM Mixtral 8x7b on GCP. I have a VM with two A100 80GBs, and am using the following setup: docker image: vllm/vllm-openai:v0.3.0 Model: mistralai/Mixtral-8x7B-Instruct-v0.1 Command I use inside the vm: python3 -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x7B-Instruct-v0.1 --tensor-parallel-size 2 --port 8888 Output (after a while): ``` File "/usr/local/lib/python3.10/dist-packages/torch/nn/functional.py", line 1858, in softmax ret = input.softmax(dim, dtype=dtype) RuntimeError: CUDA error: invalid device function ``` nvidia-smi output: ``` +-----------------------------------------------------------------------------+ | NVIDIA-SMI 525.105.17 Driver Version: 525.105.17 CUDA Version: 12.0 | |-------------------------------+----------------------+----------------------+ | GPU Name Persistence-M| Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap| Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |===============================+======================+======================| | 0 NVIDIA A100-SXM... Off | 00000000:00:06.0 Off | 0 | | N/A 32C P0 62W / 400W | 0MiB / 81920MiB | 0% Default | | | | Disabled | +--------------...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: GCP. I have a VM with two A100 80GBs, and am using the following setup: docker image: vllm/vllm-openai:v0.3.0 Model: mistralai/Mixtral-8x7B-Instruct-v0.1 Command I use inside the vm: python3 -m vllm.entrypoints.openai.a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: Hi, I am trying to set up vLLM Mixtral 8x7b on GCP. I have a VM with two A100 80GBs, and am using the following setup: docker image: vllm/vllm-openai:v0.3.0 Model: mistralai/Mixtral-8x7B-Instruct-v0.1 Command I use insi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ch/nn/functional.py", line 1858, in softmax ret = input.softmax(dim, dtype=dtype) RuntimeError: CUDA error: invalid device function ``` nvidia-smi output: ``` +-----------------------------------------------------------...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: and am using the following setup: docker image: vllm/vllm-openai:v0.3.0 Model: mistralai/Mixtral-8x7B-Instruct-v0.1 Command I use inside the vm: python3 -m vllm.entrypoints.openai.api_server --model mistralai/Mixtral-8x...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: --tensor-parallel-size 2 fails to load on GCP stale Hi, I am trying to set up vLLM Mixtral 8x7b on GCP. I have a VM with two A100 80GBs, and am using the following setup: docker image: vllm/vllm-openai:v0.3.0 Model: mis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

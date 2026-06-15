# vllm-project/vllm#22007: [Usage]: ModuleNotFoundError: No module named 'vllm.vllm_flash_attn.layers'

| 字段 | 值 |
| --- | --- |
| Issue | [#22007](https://github.com/vllm-project/vllm/issues/22007) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash;import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: ModuleNotFoundError: No module named 'vllm.vllm_flash_attn.layers'

### Issue 正文摘录

### Your current environment Host environment ```text Linux ubuntu 6.8.0-63-generic #66-Ubuntu SMP PREEMPT_DYNAMIC Fri Jun 13 20:09:49 UTC 2025 aarch64 aarch64 aarch64 GNU/Linux NVIDIA-SMI 575.64.03 Driver Version: 575.64.03 CUDA Version: 12.9 ``` I successfully built the Docker image locally: ``` DOCKER_BUILDKIT=1 docker build . \ --file docker/Dockerfile \ --target vllm-openai \ --platform "linux/arm64" \ -t vllm/vllm-ada-openai:latest \ --build-arg max_jobs=96 \ --build-arg nvcc_threads=2 \ --build-arg torch_cuda_arch_list="8.9" \ --build-arg vllm_fa_cmake_gpu_arches="89-real" \ --build-arg RUN_WHEEL_CHECK=false \ --build-arg PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple \ --build-arg PYTORCH_CUDA_INDEX_BASE_URL=https://mirrors.aliyun.com/pytorch-wheels ``` But error occurred during docker run. Error message: ``` (APIServer pid=1) 2025-07-31 03:11:49,578 - modelscope - INFO - Target directory already exists, skipping creation. (APIServer pid=1) 2025-07-31 03:11:50,488 - modelscope - INFO - Target directory already exists, skipping creation. (APIServer pid=1) Downloading Model from https://www.modelscope.cn to directory: /root/.cache/modelscope/hub/models/Qwen/Qwen3-0.6...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rch64 aarch64 aarch64 GNU/Linux NVIDIA-SMI 575.64.03 Driver Version: 575.64.03 CUDA Version: 12.9 ``` I successfully built the Docker image locally: ``` DOCKER_BUILDKIT=1 docker build . \ --file docker/Dockerfile \ --ta...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: er run. Error message: ``` (APIServer pid=1) 2025-07-31 03:11:49,578 - modelscope - INFO - Target directory already exists, skipping creation. (APIServer pid=1) 2025-07-31 03:11:50,488 - modelscope - INFO - Target direc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ment Host environment ```text Linux ubuntu 6.8.0-63-generic #66-Ubuntu SMP PREEMPT_DYNAMIC Fri Jun 13 20:09:49 UTC 2025 aarch64 aarch64 aarch64 GNU/Linux NVIDIA-SMI 575.64.03 Driver Version: 575.64.03 CUDA Version: 12.9...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ls. [type=value_error, input_value=ArgsKwargs((), {'model': ...attention_dtype': None}), input_type=ArgsKwargs] (APIServer pid=1) For further information visit https://errors.pydantic.dev/2.11/v/value_error ``` ### How...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: arg vllm_fa_cmake_gpu_arches="89-real" \ --build-arg RUN_WHEEL_CHECK=false \ --build-arg PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple \ --build-arg PYTORCH_CUDA_INDEX_BASE_URL=https://mirrors.aliyun.com/pytorc...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

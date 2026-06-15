# vllm-project/vllm#28486: [Installation]: No pre-built wheel available in 0.11.0

| 字段 | 值 |
| --- | --- |
| Issue | [#28486](https://github.com/vllm-project/vllm/issues/28486) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;quantization |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: No pre-built wheel available in 0.11.0

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` N/A: running google colab T4 3.12 CUDA 12.6 ### How you are installing vllm ```sh # Install vLLM with a specific CUDA version (e.g., 11.8 or 12.6). export VLLM_VERSION=$(curl -s https://api.github.com/repos/vllm-project/vllm/releases/latest | jq -r .tag_name | sed 's/^v//') export CUDA_VERSION=118 # or 126 uv pip install https://github.com/vllm-project/vllm/releases/download/v${VLLM_VERSION}/vllm-${VLLM_VERSION}+cu${CUDA_VERSION}-cp38-abi3-manylinux1_x86_64.whl --extra-index-url https://download.pytorch.org/whl/cu${CUDA_VERSION} ``` I am trying to download vLLM for google colab to run AWQ model. As the default wheel is compiled for CUDA12.8, I need to download an older model as AWQ seems to fail on current setup. **But**, there is no wheel binary as mentioned in the documentation and since I am using colab, I am quite limited in my build options. Snippet coming from [docs](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/#pre-built-wheels) `As of now, vLLM's binaries are compiled with CUDA 12.8 and public PyTorch release versions by default. We also provide vLLM binaries compiled with CUD...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Installation]: No pre-built wheel available in 0.11.0 installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` N/A: running google colab T4 3.12 CUDA 12.6 ### How you are insta
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: output of `python collect_env.py` ``` N/A: running google colab T4 3.12 CUDA 12.6 ### How you are installing vllm ```sh # Install vLLM with a specific CUDA version (e.g., 11.8 or 12.6). export VLLM_VERSION=$(curl -s htt...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: quently asked questions. development ci_build;frontend_api;model_support;quantization cuda;quantization build_error env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: A_VERSION} ``` I am trying to download vLLM for google colab to run AWQ model. As the default wheel is compiled for CUDA12.8, I need to download an older model as AWQ seems to fail on current setup. **But**, there is no...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Installation]: No pre-built wheel available in 0.11.0 installation;stale ### Your current environment ```text The output of `python collect_env.py` ``` N/A: running google colab T4 3.12 CUDA 12.6 ### How you are instal...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

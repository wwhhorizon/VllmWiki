# vllm-project/vllm#11731: [Usage]: serving  'LLaVA-Next-Video-7B-Qwen2'

| 字段 | 值 |
| --- | --- |
| Issue | [#11731](https://github.com/vllm-project/vllm/issues/11731) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: serving  'LLaVA-Next-Video-7B-Qwen2'

### Issue 正文摘录

`conda env python=3.12` _libgcc_mutex 0.1 main _openmp_mutex 5.1 1_gnu absl-py 2.1.0 pypi_0 pypi accelerate 1.0.1 pypi_0 pypi aiohappyeyeballs 2.4.3 pypi_0 pypi aiohttp 3.10.10 pypi_0 pypi aiohttp-cors 0.7.0 pypi_0 pypi aiosignal 1.3.1 pypi_0 pypi airportsdata 20241001 pypi_0 pypi annotated-types 0.7.0 pypi_0 pypi anyio 4.6.2.post1 pypi_0 pypi argcomplete 3.5.1 pypi_0 pypi astor 0.8.1 pypi_0 pypi attrs 24.2.0 pypi_0 pypi audioread 3.0.1 pypi_0 pypi awscli 1.35.23 pypi_0 pypi bitsandbytes 0.45.0 pypi_0 pypi black 24.10.0 pypi_0 pypi blake3 1.0.0 pypi_0 pypi boto3 1.35.57 pypi_0 pypi botocore 1.35.57 pypi_0 pypi buildkite-test-collector 0.1.9 pypi_0 pypi bzip2 1.0.8 h5eee18b_6 c-ares 1.19.1 h5eee18b_0 ca-certificates 2024.11.26 h06a4308_0 cachetools 5.5.0 pypi_0 pypi certifi 2024.8.30 pypi_0 pypi cffi 1.17.1 pypi_0 pypi chardet 5.2.0 pypi_0 pypi charset-normalizer 3.4.0 pypi_0 pypi clang-format 18.1.5 pypi_0 pypi click 8.1.7 pypi_0 pypi cloudpickle 3.1.0 pypi_0 pypi cmake 3.31.2 pypi_0 pypi codespell 2.3.0 pypi_0 pypi colorama 0.4.6 pypi_0 pypi colorful 0.5.6 pypi_0 pypi compressed-tensors 0.8.1 pypi_0 pypi contourpy 1.3.0 pypi_0 pypi cupy-cuda12x 13.3.0 pypi_0 pypi cycler 0.12.1 py...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: pypi botocore 1.35.57 pypi_0 pypi buildkite-test-collector 0.1.9 pypi_0 pypi bzip2 1.0.8 h5eee18b_6 c-ares 1.19.1 h5eee18b_0 ca-certificates 2024.11.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Usage]: serving 'LLaVA-Next-Video-7B-Qwen2' usage `conda env python=3.12` _libgcc_mutex 0.1 main _openmp_mutex 5.1 1_gnu absl-py 2.1.0 pypi_0 p
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: i contourpy 1.3.0 pypi_0 pypi cupy-cuda12x 13.3.0 pypi_0 pypi cycler 0.12.1 pypi_0 pypi datamodel-code-generator 0.26.3 pypi_0 pypi dataproperty 1
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: a 3.10 pypi_0 pypi importlib-metadata 8.5.0 pypi_0 pypi inflect 5.6.2 pypi_0 pypi iniconfig 2.0.0 pypi_0 pypi interegular 0.3.3
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: i matplotlib 3.9.2 pypi_0 pypi mbstrdecoder 1.1.3 pypi_0 pypi mdit-py-plugins 0.4.2 pypi_0 pypi mdurl 0.1.2 pypi_0 pypi memray 1

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

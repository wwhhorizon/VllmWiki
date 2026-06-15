# vllm-project/vllm#602: pip install fails with CUDA version (12.0) mismatch compile  PyTorch (11.7). though I am using torch (2.1.0.dev20230726+cu121)

| 字段 | 值 |
| --- | --- |
| Issue | [#602](https://github.com/vllm-project/vllm/issues/602) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build |
| 子分类 | wrong_output |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> pip install fails with CUDA version (12.0) mismatch compile  PyTorch (11.7). though I am using torch (2.1.0.dev20230726+cu121)

### Issue 正文摘录

I have the torch version `2.1.0.dev20230726+cu121` installed from nightly, (pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121) ``` import torch print(torch.__version__) print(torch.version.cuda) ``` ``` 2.1.0.dev20230726+cu121 12.1 ``` However `pip install vllm` fails with ``` File "/tmp/pip-build-env-k_b5x9gx/overlay/local/lib/python3.10/dist-packages/torch/utils/cpp_extension.py", line 499, in build_extensions _check_cuda_version(compiler_name, compiler_version) File "/tmp/pip-build-env-k_b5x9gx/overlay/local/lib/python3.10/dist-packages/torch/utils/cpp_extension.py", line 387, in _check_cuda_version raise RuntimeError(CUDA_MISMATCH_MESSAGE.format(cuda_str_version, torch.version.cuda)) RuntimeError: The detected CUDA version (12.0) mismatches the version that was used to compile PyTorch (11.7). Please make sure to use the same CUDA versions. [end of output] ```

## 现有链接修复摘要

#36810 [ROCm][Perf] Fused GEMM + static FP8 output quantization

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: pip install fails with CUDA version (12.0) mismatch compile PyTorch (11.7). though I am using torch (2.1.0.dev20230726+cu121) I have the torch version `2.1.0.dev20230726+cu121` installed from nightly, (pip3 install --pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: pip install fails with CUDA version (12.0) mismatch compile PyTorch (11.7). though I am using torch (2.1.0.dev20230726+cu121) I have the torch version `2.1.0.dev20230726+cu121` installed from nightly, (pip3 install --pr...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ld_error;mismatch env_dependency #36810 [ROCm][Perf] Fused GEMM + static FP8 output quantization I have the torch version `2.1.0.dev20230726+cu121` installed from nightly, (pip3 install --pre torch torchvision torchaudi...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: pip install fails with CUDA version (12.0) mismatch compile PyTorch (11.7). though I am using torch (2.1.0.dev20230726+cu121) I have the torch version `2.1.0.dev20230726+cu121` installed from nightly, (pip3 install --pr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n _check_cuda_version raise RuntimeError(CUDA_MISMATCH_MESSAGE.format(cuda_str_version, torch.version.cuda)) RuntimeError: The detected CUDA version (12.0) mismatches the version that was used to compile PyTorch (11.7)....

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36810](https://github.com/vllm-project/vllm/pull/36810) | mentioned | 0.6 | [ROCm][Perf] Fused GEMM + static FP8 output quantization | use **hipBLASLt natively supports FP8 output dtype** since ROCm 6.0 ([ROCm/hipBLASLt#602](https://github.com/ROCm/hipBLASLt/pull/602)). ```python # Before (2 kernels + BF16 round-… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#36382: [CPU] AssertionError in CPUModelRunner: device_tensor type mismatch (numpy.ndarray)

| 字段 | 值 |
| --- | --- |
| Issue | [#36382](https://github.com/vllm-project/vllm/issues/36382) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CPU] AssertionError in CPUModelRunner: device_tensor type mismatch (numpy.ndarray)

### Issue 正文摘录

## Environment - **OS**: macOS (Apple Silicon/ARM64) - CPU Mode - **Python**: 3.13 - **vLLM Version**: `0.1.dev14590+g5d6aae457` (Commit: `5d6aae4577590cd6b6a604f9e74c17c5f234271d`) - **PyTorch Version**: `2.10.0` - **Installation Method**: Editable build (`pip install -e .`) ## Description When running the V1 engine on CPU with `VLLM_TARGET_DEVICE=cpu` and `VLLM_ENABLE_V1_MULTIPROCESSING=0`, an `AssertionError` occurs in `vllm.v1.worker.cpu_model_runner.CPUModelRunner`. The error happens during the initialization of the runner when it attempts to replace tensor attributes. The code expects `device_tensor` to be a `torch.Tensor`, but for some attributes (specifically `num_tokens_no_spec`), it is initialized as a `numpy.ndarray`. ## Reproduction Script (`hello_world.py`) ```python from vllm import LLM, SamplingParams from vllm.sampling_params import StructuredOutputsParams my_schema = { "type": "object", "properties": { "greeting": {"type": "string"}, "name": {"type": "string"} }, "required": ["greeting", "name"] } if __name__ == "__main__": # Force CPU and disable multiprocessing (to avoid spawn issues on macOS) # Env vars: VLLM_TARGET_DEVICE=cpu VLLM_ENABLE_V1_MULTIPROCESSING=0 l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: OS**: macOS (Apple Silicon/ARM64) - CPU Mode - **Python**: 3.13 - **vLLM Version**: `0.1.dev14590+g5d6aae457` (Commit: `5d6aae4577590cd6b6a604f9e74c17c5f234271d`) - **PyTorch Version**: `2.10.0` - **Installation Method*...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [CPU] AssertionError in CPUModelRunner: device_tensor type mismatch (numpy.ndarray) ## Environment - **OS**: macOS (Apple Silicon/ARM64) - CPU Mode - **Python**: 3.13 - **vLLM Version**: `0.1.dev14590+g5d6aae457` (Commi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [CPU] AssertionError in CPUModelRunner: device_tensor type mismatch (numpy.ndarray) ## Environment - **OS**: macOS (Apple Silicon/ARM64) - CPU Mode - **Python**: 3.13 - **vLLM Version**: `0.1.dev14590+g5d6aae457` (Commi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [CPU] AssertionError in CPUModelRunner: device_tensor type mismatch (numpy.ndarray) ## Environment - **OS**: macOS (Apple Silicon/ARM64) - CPU Mode - **Python**: 3.13 - **vLLM Version**: `0.1.dev14590+g5d6aae457` (Commi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

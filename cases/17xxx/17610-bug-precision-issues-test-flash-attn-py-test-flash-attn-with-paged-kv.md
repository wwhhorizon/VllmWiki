# vllm-project/vllm#17610: [Bug]: [Precision issues] test_flash_attn.py::test_flash_attn_with_paged_kv

| 字段 | 值 |
| --- | --- |
| Issue | [#17610](https://github.com/vllm-project/vllm/issues/17610) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;triton |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Precision issues] test_flash_attn.py::test_flash_attn_with_paged_kv

### Issue 正文摘录

### Your current environment vllm: 0.7.4 CUDA Version: 12.5 device: NVIDIA A100-PCIE-40GB When implementing the flash_attn_with_kvcache method using Triton operators, precision issues were observed. Therefore, we invoked the test cases built into vLLM with corresponding data for validation, and found that the test cases also failed. cmd: pytest -s -v tests/kernels/test_flash_attn.py::test_flash_attn_with_paged_kv ### 🐛 Describe the bug ERROR message: AssertionError: Tensor-likes are not close! E E Mismatched elements: 1 / 14336 (0.0%) E Greatest absolute difference: 0.037109375 at index (2, 1, 26) (up to 0.02 allowed) E Greatest relative difference: 0.07568359375 at index (2, 1, 26) (up to 0.01 allowed) detail value: output[2, 1, 26]==== tensor(-0.4902, device='cuda:0', dtype=torch.bfloat16) ref_output[2, 1, 26]==== tensor(-0.5273, device='cuda:0', dtype=torch.bfloat16) Detail inputs for the test @pytest.mark.parametrize("use_out", [True]) @pytest.mark.parametrize("kv_lens", [[7,9,7,7]]) @pytest.mark.parametrize("num_heads" ,[[28,4]]) @pytest.mark.parametrize("head_size", [128]) @pytest.mark.parametrize("block_size", [16]) @pytest.mark.parametrize("dtype", [torch.bfloat16]) @pytes...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: h_attn_with_paged_kv bug;stale ### Your current environment vllm: 0.7.4 CUDA Version: 12.5 device: NVIDIA A100-PCIE-40GB When implementing the flash_attn_with_kvcache method using Triton operators, precision issues were...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: [Precision issues] test_flash_attn.py::test_flash_attn_with_paged_kv bug;stale ### Your current environment vllm: 0.7.4 CUDA Version: 12.5 device: NVIDIA A100-PCIE-40GB When implementing the flash_attn_with_kvcac...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: wed) detail value: output[2, 1, 26]==== tensor(-0.4902, device='cuda:0', dtype=torch.bfloat16) ref_output[2, 1, 26]==== tensor(-0.5273, device='cuda:0', dtype=torch.bfloat16) Detail inputs for the test @pytest.mark.para...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: [Precision issues] test_flash_attn.py::test_flash_attn_with_paged_kv bug;stale ### Your current environment vllm: 0.7.4 CUDA Version: 12.5 device: NVIDIA A100-PCIE-40GB When implementing the flash_attn_with_kvcac...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Precision issues] test_flash_attn.py::test_flash_attn_with_paged_kv bug;stale ### Your current environment vllm: 0.7.4 CUDA Version: 12.5 device: NVIDIA A100-PCIE-40GB When implementing the flash_attn_with_kvcache meth...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

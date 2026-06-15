# vllm-project/vllm#1486: Array Index Overflow for Large #Blocks

| 字段 | 值 |
| --- | --- |
| Issue | [#1486](https://github.com/vllm-project/vllm/issues/1486) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 |  |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;kernel |
| 症状 | nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Array Index Overflow for Large #Blocks

### Issue 正文摘录

Suppose we have 64K blocks, and the key cache shape of a single layer is `[64K, 32, 16, 16, 8]` (LLaMA-7B). For slot mapping, the maximum value is `64K * 32 * 16 * 16 * 8 = 4194304K > INT_MAX`, which overflow. ## Env `PyTorch 2.0.1 + vLLM 0.2.0 + cuda-11.7` ## Simple reproduce We can reproduce this by changing the parameters of `tests/kernels/test_cache.py` to the following ``` DTYPES = [torch.half] NUM_TOKENS = [7] # Arbitrary values for testing NUM_LAYERS = [1] # Arbitrary values for testing NUM_HEADS = [32] # Arbitrary values for testing HEAD_SIZES = [128] BLOCK_SIZES = [16] NUM_BLOCKS = [64000] # Arbitrary values for testing NUM_MAPPINGS = [32] # Arbitrary values for testing SEEDS = [0] ``` The `reshape_and_cache` kernel cannot pass the test. If we change the dtype of `slot_mapping` to int64, we can pass the test. Besides, change `NUM_BLOCKS` to 64K in `tests/kernels/test_attention.py`, I find it cannot pass the test, either. It reports "illegal memory access". @zhuohan123 @WoosukKwon Can you help look into this?

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: Array Index Overflow for Large #Blocks bug Suppose we have 64K blocks, and the key cache shape of a single layer is `[64K, 32, 16, 16, 8]` (LLaMA-7B). For slot mapping, the maximum value is `64K * 32 * 16 * 16 * 8 = 419...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ch overflow. ## Env `PyTorch 2.0.1 + vLLM 0.2.0 + cuda-11.7` ## Simple reproduce We can reproduce this by changing the parameters of `tests/kernels/test_cache.py` to the following ``` DTYPES = [torch.half] NUM_TOKENS =...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: you help look into this? correctness cache;cuda;kernel nan_inf dtype;env_dependency;shape Suppose we have 64K blocks, and the key cache shape of a single layer is `[64K, 32, 16, 16, 8]` (LLaMA-7B). For slot mapping, the...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ing the parameters of `tests/kernels/test_cache.py` to the following ``` DTYPES = [torch.half] NUM_TOKENS = [7] # Arbitrary values for testing NUM_LAYERS = [1] # Arbitrary values for testing NUM_HEADS = [32] # Arbitrary...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 94304K > INT_MAX`, which overflow. ## Env `PyTorch 2.0.1 + vLLM 0.2.0 + cuda-11.7` ## Simple reproduce We can reproduce this by changing the parameters of `tests/kernels/test_cache.py` to the following ``` DTYPES = [tor...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

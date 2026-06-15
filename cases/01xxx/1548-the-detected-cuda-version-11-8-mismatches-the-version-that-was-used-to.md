# vllm-project/vllm#1548:  The detected CUDA version (11.8) mismatches the version that was used to compile       PyTorch (12.1). Please make sure to use the same CUDA versions.

| 字段 | 值 |
| --- | --- |
| Issue | [#1548](https://github.com/vllm-project/vllm/issues/1548) |
| 状态 | closed |
| 标签 |  |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 | build_error;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

>  The detected CUDA version (11.8) mismatches the version that was used to compile       PyTorch (12.1). Please make sure to use the same CUDA versions.

### Issue 正文摘录

Hi guys, I install vllm failed with pip install -e . The error messages shows below: ``` RuntimeError: The detected CUDA version (11.8) mismatches the version that was used to compile PyTorch (12.1). Please make sure to use the same CUDA versions. ``` My driver version is 535.113.01 and cuda version is 11.8，python version is 3.8. ![image](https://github.com/vllm-project/vllm/assets/87475073/2096c9a5-b869-4d84-be1f-0b7e61072f9a) I have no idea about this issue, even though I pre-install pytorch=2.0.1+cu11.8, it still failed. Will appreciate some help on it.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: The detected CUDA version (11.8) mismatches the version that was used to compile PyTorch (12.1). Please make sure to use the same CUDA versions. Hi guys, I install vllm failed with pip install -e . The error messages sh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: The detected CUDA version (11.8) mismatches the version that was used to compile PyTorch (12.1). Please make sure to use the same CUDA versions. Hi guys, I install vllm failed with pip install -e . The error messages sh...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: The detected CUDA version (11.8) mismatches the version that was used to compile PyTorch (12.1). Please make sure to use the same CUDA versions. Hi guys, I install vllm failed with pip install -e . The error messages sh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

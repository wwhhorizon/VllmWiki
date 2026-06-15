# vllm-project/vllm#34464: [CI Failure]: Ascend NPU Test

| 字段 | 值 |
| --- | --- |
| Issue | [#34464](https://github.com/vllm-project/vllm/issues/34464) |
| 状态 | open |
| 标签 | stale;ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Ascend NPU Test

### Issue 正文摘录

### Name of failing test `vllm-ascend/tests/e2e/conftest.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is likely a test infrastructure issue. The CI test fails with `ModuleNotFoundError: No module named 'torchaudio'` ``` ImportError while loading conftest '/workspace/vllm-ascend/tests/e2e/conftest.py'. -- tests/e2e/conftest.py:70: in adapt_patch(False) vllm_ascend/utils.py:356: in adapt_patch from vllm_ascend.patch import worker # noqa: F401 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ vllm_ascend/patch/worker/__init__.py:36: in import vllm_ascend.patch.worker.patch_huanyuan_vl # noqa ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ vllm_ascend/patch/worker/patch_huanyuan_vl.py:18: in from vllm.transformers_utils.processors.hunyuan_vl import HunYuanVLProcessor ../vllm/vllm/transformers_utils/processors/__init__.py:13: in from vllm.transformers_utils.processors.funasr_processor import FunASRProcessor ../vllm/vllm/transformers_utils/processors/funasr_processor.py:8: in import torchaudio.compliance.kaldi as kaldi E ModuleNotFoundError: No module named 'torchaudio' ``...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [CI Failure]: Ascend NPU Test stale;ci-failure ### Name of failing test `vllm-ascend/tests/e2e/conftest.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bu
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ests/e2e/conftest.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test This is likely a test infrastructu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: /tests/e2e/conftest.py'. -- tests/e2e/conftest.py:70: in adapt_patch(False) vllm_ascend/utils.py:356: in adapt_patch from vllm_ascend.patch import worker # noqa: F401 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ vllm_ascend/pat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: # Name of failing test `vllm-ascend/tests/e2e/conftest.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI Failure]: Ascend NPU Test stale;ci-failure ### Name of failing test `vllm-ascend/tests/e2e/conftest.py` ### Basic information - [ ] Flaky test - [ ] Can reproduce locally - [ ] Caused by external libraries (e.g. bug...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

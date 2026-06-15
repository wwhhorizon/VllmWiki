# vllm-project/vllm#34323: [CI Failure]: Spawned tests can fail silently

| 字段 | 值 |
| --- | --- |
| Issue | [#34323](https://github.com/vllm-project/vllm/issues/34323) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: Spawned tests can fail silently

### Issue 正文摘录

### Name of failing test tests/models/multimodal/generation/test_whisper.py::test_models ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test To clarify, this test is not currently failing. The issue here is that it is an example of a test that will fail silently. A recent [issue](https://github.com/vllm-project/vllm/issues/34002) broke Whisper inference and should have been picked up by test_whisper.py. We investigated why this test still seemed to pass when the model was generating nothing but whitespace. It appears to be an issue with spawning processes in tests. Forking a process works fine. Running the below on commit `a32cb49b60688fb64a6d3d7f86378b4d2fad06e6`: ``` python -m pytest -x -v -s tests/models/multimodal/generation/test_whisper.py -m cpu_model ``` The test appears to pass. If you block spawning with RUNNING_IN_SUBPROCESS=1: ``` RUNNING_IN_SUBPROCESS=1 python -m pytest -x -v -s tests/models/multimodal/generation/test_whisper.py -m cpu_model ``` then you see the test fail. This is due to the annotation ```@create_new_process_for_each_test("spawn")``` and the c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: awned tests can fail silently ci-failure ### Name of failing test tests/models/multimodal/generation/test_whisper.py::test_models ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by extern...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: isper.py::test_models ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test To clarify, this test is not curre...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [CI Failure]: Spawned tests can fail silently ci-failure ### Name of failing test tests/models/multimodal/generation/test_whisper.py::test_models ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ]
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: file with no main function calling the appropriate tests. It will affect rocm and xpu platforms especially, as the default for ```@create_new_process_for_each_test()``` is to spawn (fork for other platforms). ### 📝 Hist...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ration/test_whisper.py -m cpu_model ``` The test appears to pass. If you block spawning with RUNNING_IN_SUBPROCESS=1: ``` RUNNING_IN_SUBPROCESS=1 python -m pytest -x -v -s tests/models/multimodal/generation/test_whisper...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#9099: [Bug]: Llama-3.2-11B-Vision-Instruct which is an encoder-decoder model fails with BlockManager V2

| 字段 | 值 |
| --- | --- |
| Issue | [#9099](https://github.com/vllm-project/vllm/issues/9099) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Llama-3.2-11B-Vision-Instruct which is an encoder-decoder model fails with BlockManager V2

### Issue 正文摘录

### Your current environment The tests fail on all envs ### Model Input Dumps _No response_ ### 🐛 Describe the bug The following 2 tests fail with BlockManagerV2 - tests/models/encoder_decoder/vision_language/test_mllama.py::test_models[5-128-bfloat16-sizes0-meta-llama/Llama-3.2-11B-Vision-Instruct] - tests/models/encoder_decoder/vision_language/test_mllama.py::test_models[5-128-bfloat16-sizes4-meta-llama/Llama-3.2-11B-Vision-Instruct] The test fail with the following error ``` Traceback (most recent call last): File "/home/jovyan/sroy-enc-dec-blk-mgr-fix/tests/utils.py", line 443, in wrapper f(*args, **kwargs) File "/home/jovyan/sroy-enc-dec-blk-mgr-fix/tests/models/encoder_decoder/vision_language/test_mllama.py", line 249, in test_models run_test( File "/home/jovyan/sroy-enc-dec-blk-mgr-fix/tests/models/encoder_decoder/vision_language/test_mllama.py", line 138, in run_test _run_test( File "/home/jovyan/sroy-enc-dec-blk-mgr-fix/tests/models/encoder_decoder/vision_language/test_mllama.py", line 187, in _run_test vllm_outputs_per_image = [ File "/home/jovyan/sroy-enc-dec-blk-mgr-fix/tests/models/encoder_decoder/vision_language/test_mllama.py", line 188, in vllm_model.generate_greed...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Llama-3.2-11B-Vision-Instruct which is an encoder-decoder model fails with BlockManager V2 bug ### Your current environment The tests fail on all envs ### Model Input Dumps _No response_ ### 🐛 Describe the bug Th...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: models/encoder_decoder/vision_language/test_mllama.py::test_models[5-128-bfloat16-sizes0-meta-llama/Llama-3.2-11B-Vision-Instruct] - tests/models/encoder_decoder/vision_language/test_mllama.py::test_models[5-128-bfloat1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Llama-3.2-11B-Vision-Instruct which is an encoder-decoder model fails with BlockManager V2 bug ### Your current environment The tests fail on all envs ### Model Input Dumps _No response_ ### 🐛 Describe the bug Th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: nm ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ama-3.2-11B-Vision-Instruct which is an encoder-decoder model fails with BlockManager V2 bug ### Your current environment The tests fail on all envs ### Model Input Dumps _No response_ ### 🐛 Describe the bug The followi...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

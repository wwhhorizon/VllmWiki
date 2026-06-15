# vllm-project/vllm#34969: [CI Failure]: LM Eval Small Models (B200) - DeepSeek and Qwen3 Next

| 字段 | 值 |
| --- | --- |
| Issue | [#34969](https://github.com/vllm-project/vllm/issues/34969) |
| 状态 | closed |
| 标签 | ci-failure |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [CI Failure]: LM Eval Small Models (B200) - DeepSeek and Qwen3 Next

### Issue 正文摘录

### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test ``` FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8] - AssertionError: GSM8K metric too low: 0.0114 = (0.72 - 0.08) FAILED evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[Qwen3-Next-80B-A3B-NVFP4-EP2] - AssertionError: GSM8K metric too low: 0.0000 = (0.75 - 0.08) ``` DeepSeek just gets bad results while Qwen3-Next crashes due to ``` (Worker_TP0_EP0 pid=5870) ERROR 02-20 15:09:44 [multiproc_executor.py:867] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 3485, in execute_model (Worker_TP0_EP0 pid=5870) ERROR 02-20 15:09:44 [multiproc_executor.py:867] self._build_attention_metadata( (Worker_TP0_EP0 pid=5870) ERROR 02-20 15:09:44 [multiproc_executor.py:867] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/worker/gpu_model_runner.py", line 1888, in _build_attention_metadata (Worker_TP0_EP0 pid=5870)...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: t_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Des...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [CI Failure]: LM Eval Small Models (B200) - DeepSeek and Qwen3 Next ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic informatio...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [CI Failure]: LM Eval Small Models (B200) - DeepSeek and Qwen3 Next ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic informatio
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [CI Failure]: LM Eval Small Models (B200) - DeepSeek and Qwen3 Next ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic informatio...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [CI Failure]: LM Eval Small Models (B200) - DeepSeek and Qwen3 Next ci-failure ### Name of failing test `evals/gsm8k/test_gsm8k_correctness.py::test_gsm8k_correctness[DeepSeek-V2-Lite-Instruct-FP8]` ### Basic informatio...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

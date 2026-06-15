# vllm-project/vllm#12072: [Bug]: ValueError: Model architectures ['Qwen2AudioForConditionalGeneration'] failed to be inspected. Please check the logs for more details.

| 字段 | 值 |
| --- | --- |
| Issue | [#12072](https://github.com/vllm-project/vllm/issues/12072) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: Model architectures ['Qwen2AudioForConditionalGeneration'] failed to be inspected. Please check the logs for more details.

### Issue 正文摘录

### Your current environment @DarkLight1337 我测试了vllm的 v0.6.4 v0.6.5 v0.6.6 都无法启动qwen2-Aduio 使用的环境都是官方的 docker pull vllm/vllm-openai 对应版本 查看了相关issues 降低Numpy到v1.x 但是官方的Numpy就是1.26.4 并没有效果 ### Model Input Dumps Qwen2-Audio-7B-Instruct ### 🐛 Describe the bug # v0.6.4的报错是： WARNING 01-14 23:14:06 config.py:1865] Casting torch.bfloat16 to torch.float16. ERROR 01-14 23:14:12 registry.py:297] Error in inspecting model architecture 'Qwen2AudioForConditionalGeneration' ERROR 01-14 23:14:12 registry.py:297] Traceback (most recent call last): ERROR 01-14 23:14:12 registry.py:297] File "/usr/local/lib/python3.12/dist-packages/vllm/model_executor/models/registry.py", line 468, in _run_in_subprocess ERROR 01-14 23:14:12 registry.py:297] returned.check_returncode() ERROR 01-14 23:14:12 registry.py:297] File "/usr/lib/python3.12/subprocess.py", line 502, in check_returncode ERROR 01-14 23:14:12 registry.py:297] raise CalledProcessError(self.returncode, self.args, self.stdout, ERROR 01-14 23:14:12 registry.py:297] subprocess.CalledProcessError: Command '['/usr/bin/python3', '-m', 'vllm.model_executor.models.registry']' returned non-zero exit status 1. ERROR 01-14 23:14:12 registry.py:297] ERROR 01-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: ValueError: Model architectures ['Qwen2AudioForConditionalGeneration'] failed to be inspected. Please check the logs for more details. bug ### Your current environment @DarkLight1337 我测试了vllm的 v0.6.4 v0.6.5 v0.6....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: arkLight1337 我测试了vllm的 v0.6.4 v0.6.5 v0.6.6 都无法启动qwen2-Aduio 使用的环境都是官方的 docker pull vllm/vllm-openai 对应版本 查看了相关issues 降低Numpy到v1.x 但是官方的Numpy就是1.26.4 并没有效果 ### Model Input Dumps Qwen2-Audio-7B-Instruct ### 🐛 Describe th...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ne 202, in determine_num_available_blocks [rank0]: self.model_runner.profile_run() [rank0]: File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context [rank0]: return func(*...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: bug # v0.6.4的报错是： WARNING 01-14 23:14:06 config.py:1865] Casting torch.bfloat16 to torch.float16. ERROR 01-14 23:14:12 registry.py:297] Error in inspecting model architecture 'Qwen2AudioForConditionalGeneration' ERROR 0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Bug]: ValueError: Model architectures ['Qwen2AudioForConditionalGeneration'] failed to be inspected. Please check the logs for more details. bug ### Your current environment @DarkLight1337 我测试了vllm的 v0.6.4 v0.6.5 v0.6....

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#12771: [Bug]: Cast error details: Unable to cast 1024 to Tensor

| 字段 | 值 |
| --- | --- |
| Issue | [#12771](https://github.com/vllm-project/vllm/issues/12771) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Cast error details: Unable to cast 1024 to Tensor

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 在升级V1版本vllm后运行下面代码遇到报错： import subprocess import os my_env = os.environ.copy() my_env["VLLM_USE_V1"] = "1" command = [ "python", "-m", "vllm.scripts", "serve", "./pretrained/intervl2-8B", "--served-model-name", "intervl2-8B", "--tensor_parallel_size", "2", "--limit-mm-per-prompt","image=10" , "--pipeline-parallel-size","1", "--gpu_memory_utilization", "0.9", "--port", "40004", "--max-num-batched-tokens", "10000", "--max-seq-len-to-capture", "10000", "--max-model-len", "10000", "--enable_prefix_caching", "--trust_remote_code" ] process = subprocess.Popen(command, env=my_env) ![Image](https://github.com/user-attachments/assets/9aff0e5a-bbaa-4d23-bed0-d7f35c658531) 但是--tensor_parallel_size"设置为1的时候运行正常，是v1版本对于多卡部署模型存在兼容性问题吗 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: current environment ### 🐛 Describe the bug 在升级V1版本vllm后运行下面代码遇到报错： import subprocess import os my_env = os.environ.copy() my_env["VLLM_USE_V1"] = "1" command = [ "python", "-m", "vllm.scripts", "serve", "./pretrained/in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 问题吗 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lm.scripts", "serve", "./pretrained/intervl2-8B", "--served-model-name", "intervl2-8B", "--tensor_parallel_size", "2", "--limit-mm-per-prompt","image=10" , "--pipeline-parallel-size","1", "--gpu_memory_utilization", "0....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Cast error details: Unable to cast 1024 to Tensor bug;stale ### Your current environment ### 🐛 Describe the bug 在升级V1版本vllm后运行下面代码遇到报错： import subprocess import os my_env = os.environ.copy() my_env["VLLM_USE_V1"]...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

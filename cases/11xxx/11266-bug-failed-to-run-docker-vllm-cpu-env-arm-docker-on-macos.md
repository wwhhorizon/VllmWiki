# vllm-project/vllm#11266: [Bug]: Failed to run docker vllm-cpu-env arm docker on MacOS

| 字段 | 值 |
| --- | --- |
| Issue | [#11266](https://github.com/vllm-project/vllm/issues/11266) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Failed to run docker vllm-cpu-env arm docker on MacOS

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After building Docker Images with [Dockerfile.arm](https://docs.vllm.ai/en/latest/getting_started/arm-installation.html), it built successfully but when attempts to run `docker run -it \ --rm \ --network=host \ vllm-cpu-env --device="cpu" --disable_async_output_proc --enforce-eager --model=Qwen/Qwen2.5-1.5B-Instruct --dtype=float16`. it gets error in : `File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 1639, in resolve_obj_by_qualname module_name, obj_name = qualname.rsplit(".", 1) ` I am running on MacStudio Ultra and env is collected by building `Dockerfile.arm` file by executing `docker build -f Dockerfile.arm -t vllm-cpu-env --shm-size=4g .` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: Failed to run docker vllm-cpu-env arm docker on MacOS bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After building Docker Images with [Dockerfile.arm](https://docs.vl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: e_async_output_proc --enforce-eager --model=Qwen/Qwen2.5-1.5B-Instruct --dtype=float16`. it gets error in : `File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 1639, in resolve_obj_by_qualname module_nam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llm-cpu-env arm docker on MacOS bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug After building Docker Images with [Dockerfile.arm](https://docs.vllm.ai/en/latest/getting_start...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: .` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: r building Docker Images with [Dockerfile.arm](https://docs.vllm.ai/en/latest/getting_started/arm-installation.html), it built successfully but when attempts to run `docker run -it \ --rm \ --network=host \ vllm-cpu-env...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

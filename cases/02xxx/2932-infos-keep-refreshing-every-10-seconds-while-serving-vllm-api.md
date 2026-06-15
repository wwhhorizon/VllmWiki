# vllm-project/vllm#2932: INFOs keep refreshing every 10 seconds while serving vllm api

| 字段 | 值 |
| --- | --- |
| Issue | [#2932](https://github.com/vllm-project/vllm/issues/2932) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> INFOs keep refreshing every 10 seconds while serving vllm api

### Issue 正文摘录

vllm = 0.3.1 Here is my script: ``` CUDA_VISIBLE_DEVICES="4" python -m vllm.entrypoints.openai.api_server \ --model="./NeuralBeagle14-7B/" \ --trust-remote-code \ --tensor-parallel-size 1 \ --port 8000 \ --disable-custom-all-reduce \ ``` When there is no inputs, the terminal keeps refreshing every 10 seconds as follow: ![20240220-150902](https://github.com/vllm-project/vllm/assets/49086900/d744e205-d754-4a63-b606-489f938f9065) Is this the special setup or a bug?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lm/assets/49086900/d744e205-d754-4a63-b606-489f938f9065) Is this the special setup or a bug?
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ry 10 seconds while serving vllm api vllm = 0.3.1 Here is my script: ``` CUDA_VISIBLE_DEVICES="4" python -m vllm.entrypoints.openai.api_server \ --model="./NeuralBeagle14-7B/" \ --trust-remote-code \ --tensor-parallel-s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: VISIBLE_DEVICES="4" python -m vllm.entrypoints.openai.api_server \ --model="./NeuralBeagle14-7B/" \ --trust-remote-code \ --tensor-parallel-size 1 \ --port 8000 \ --disable-custom-all-reduce \ ``` When there is no input...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

# vllm-project/vllm#23301: [Usage]: During testing of the LoRA model, the "enable-prefix-caching" feature did not take effect

| 字段 | 值 |
| --- | --- |
| Issue | [#23301](https://github.com/vllm-project/vllm/issues/23301) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: During testing of the LoRA model, the "enable-prefix-caching" feature did not take effect

### Issue 正文摘录

### Your current environment ```text Using docker image - vllm version: 0.9.1 ``` ### How would you like to use vllm server： vllm serve /home/data/nlp/deepseek_models/DeepSeek-R1-Distill-Qwen-32B-AWQ --max-model-len 8192 --quantization awq --port 8081 --tensor-parallel-size 4 --trust-remote-code --max-num-seqs 1 --enable-lora --lora-modules r16-static=/home/data/nlp/deepseek_models/DeepSeek-R1-Distill-Qwen-32B-Lora-r16 --max_loras=2 client： python3 benchmark_serving.py --host 0.0.0.0 --port 8081 --model /home/data/nlp/deepseek_models/DeepSeek-R1-Distill-Qwen-32B-AWQ --num-prompts 1 --dataset-name random --random-input-len 2048 --random-output-len 512 --lora-modules r16-static Through the above command, the base inference 'enable prefix caching' takes effect, but the lora inference 'enable prefix caching' does not take effect. Base result： Lora result： ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: not take effect usage;stale ### Your current environment ```text Using docker image - vllm version: 0.9.1 ``` ### How would you like to use vllm server： vllm serve /home/data/nlp/deepseek_models/DeepSeek-R1-Distill-Qwen...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: During testing of the LoRA model, the "enable-prefix-caching" feature did not take effect usage;stale ### Your current environment ```text Using docker image - vllm version: 0.9.1 ``` ### How would you like to...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Usage]: During testing of the LoRA model, the "enable-prefix-caching" feature did not take effect usage;stale ### Your current environment ```text Using docker image - vllm version: 0.9.1 ``` ### How would you like to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: /deepseek_models/DeepSeek-R1-Distill-Qwen-32B-AWQ --max-model-len 8192 --quantization awq --port 8081 --tensor-parallel-size 4 --trust-remote-code --max-num-seqs 1 --enable-lora --lora-modules r16-static=/home/data/nlp/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ： ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

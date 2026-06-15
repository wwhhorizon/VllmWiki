# vllm-project/vllm#12741: [Bug]: V1 Engine Non-Coherent output

| 字段 | 值 |
| --- | --- |
| Issue | [#12741](https://github.com/vllm-project/vllm/issues/12741) |
| 状态 | closed |
| 标签 | bug;v1 |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: V1 Engine Non-Coherent output

### Issue 正文摘录

### Your current environment Vllm 0.7.1 CUDA 12.6 Driver Version 560.94 torch 2.5.1 transformers 4.46.0 ### 🐛 Describe the bug When using V1 engine, the output is noncoherent. For examples: ".SetString that a I. to . v the . the v the on the this . p et is Jansw to A 2000 v and . tochemically the I in we , (self. . v or on we Fnew, international lawrence of for000, __in U, do — and it - arse not C is images that super()000 the use a . v the . v to000 an A for to000 with from in g be for . " I have tried various changes including changing temp, frequency_penalty, etc. I have tried various models, and nothing improved. Here is what I use vllm serve nm-testing/DeepSeek-R1-Distill-Llama-70B-FP8-dynamic --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1234 --max-model-len 16000 --enable-auto-tool-choice --tool-call-parser llama3_json --chat-template /home/nd600/miniconda3/envs/vllm/lib/python3.12/site-packages/vllm/examples/tool_chat_template_llama3.1_json.jinja Thanks for your help. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vll...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gine Non-Coherent output bug;v1 ### Your current environment Vllm 0.7.1 CUDA 12.6 Driver Version 560.94 torch 2.5.1 transformers 4.46.0 ### 🐛 Describe the bug When using V1 engine, the output is noncoherent. For example...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: es including changing temp, frequency_penalty, etc. I have tried various models, and nothing improved. Here is what I use vllm serve nm-testing/DeepSeek-R1-Distill-Llama-70B-FP8-dynamic --host 0.0.0.0 --port 8000 --tens...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: output bug;v1 ### Your current environment Vllm 0.7.1 CUDA 12.6 Driver Version 560.94 torch 2.5.1 transformers 4.46.0 ### 🐛 Describe the bug When using V1 engine, the output is noncoherent. For examples: ".SetString tha...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: . Here is what I use vllm serve nm-testing/DeepSeek-R1-Distill-Llama-70B-FP8-dynamic --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1234 --max-model-len 16000 --enable-auto-tool-choice --tool-call-parser lla...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: d various models, and nothing improved. Here is what I use vllm serve nm-testing/DeepSeek-R1-Distill-Llama-70B-FP8-dynamic --host 0.0.0.0 --port 8000 --tensor-parallel-size 8 --seed 1234 --max-model-len 16000 --enable-a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

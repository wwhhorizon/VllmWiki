# vllm-project/vllm#2786: Cannot get expected model size reducing when lauching squeezellm mode

| 字段 | 值 |
| --- | --- |
| Issue | [#2786](https://github.com/vllm-project/vllm/issues/2786) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Cannot get expected model size reducing when lauching squeezellm mode

### Issue 正文摘录

Hi Everybody, I'm simply following vllm (version **0.3.0**) helper to run a squeezellm quantized llama-2 model, using following command `python3 -m vllm.entrypoints.openai.api_server --model squeeze-ai-lab/sq-llama-2-7b-w4-s0 --tensor-parallel-size 1 --max-model-len 1000 --gpu-memory-utilization 0.9 --quantization squeezellm` It runs well but `nvidia-smi` show that model is occupying **~15Gb** among the 16Gb available in my NVIDIA V100, while i expected model size to be reduced by 4. Is there something i did wrong? Does my GPU fit with squeezellm quantization requirements? Or maybe my environement has not been built the right way? Thanks for any help or any link that show successful use of llama-2 with squeezellm Regards

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: Cannot get expected model size reducing when lauching squeezellm mode Hi Everybody, I'm simply following vllm (version **0.3.0**) helper to run a squeezellm quantized llama-2 model, using following command `python3 -m v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Cannot get expected model size reducing when lauching squeezellm mode Hi Everybody, I'm simply following vllm (version **0.3.0**) helper to run a squeezellm quantized llama-2 model, using following command `python3 -m v...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: I'm simply following vllm (version **0.3.0**) helper to run a squeezellm quantized llama-2 model, using following command `python3 -m vllm.entrypoints.openai.api_server --model squeeze-ai-lab/sq-llama-2-7b-w4-s0 --tenso...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ry-utilization 0.9 --quantization squeezellm` It runs well but `nvidia-smi` show that model is occupying **~15Gb** among the 16Gb available in my NVIDIA V100, while i expected model size to be reduced by 4. Is there som...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

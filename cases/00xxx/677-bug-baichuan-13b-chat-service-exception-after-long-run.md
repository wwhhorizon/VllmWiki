# vllm-project/vllm#677: [Bug] baichuan-13b-chat Service exception after long run

| 字段 | 值 |
| --- | --- |
| Issue | [#677](https://github.com/vllm-project/vllm/issues/677) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] baichuan-13b-chat Service exception after long run

### Issue 正文摘录

Start command ``` python -m vllm.entrypoints.openai.api_server --model baichuan-inc/Baichuan-13B-Chat --host 0.0.0.0 --port 8777 --trust-remote-code --dtype half ``` After about 12 hours of operation, the inference service stopped working GPU：V100 CUDA：11.4 Screenshot of the problem： ![Xnip2023-08-05_12-03-19](https://github.com/vllm-project/vllm/assets/33508761/68f881f4-4d18-4e2f-8751-85770b5367b8)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: f4-4d18-4e2f-8751-85770b5367b8) development model_support cuda dtype;env_dependency Start command
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: n-inc/Baichuan-13B-Chat --host 0.0.0.0 --port 8777 --trust-remote-code --dtype half ``` After about 12 hours of operation, the inference service stopped working GPU：V100 CUDA：11.4 Screenshot of the problem： ![Xnip2023-0...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 12 hours of operation, the inference service stopped working GPU：V100 CUDA：11.4 Screenshot of the problem： ![Xnip2023-08-05_12-03-19](https://github.com/vllm-project/vllm/assets/33508761/68f881f4-4d18-4e2f-8751-85770b53...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: run bug Start command ``` python -m vllm.entrypoints.openai.api_server --model baichuan-inc/Baichuan-13B-Chat --host 0.0.0.0 --port 8777 --trust-remote-code --dtype half ``` After about 12 hours of operation, the infere...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。

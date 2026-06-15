# vllm-project/vllm#19414: [Doc]: can not close thinking

| 字段 | 值 |
| --- | --- |
| Issue | [#19414](https://github.com/vllm-project/vllm/issues/19414) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: can not close thinking

### Issue 正文摘录

version=0.9.0.1 set enable_thinking=True , can not close thinking CUDA_VISIBLE_DEVICES=4,5,6,7 python3 -m vllm.entrypoints.openai.api_server \ --model $modelpath \ --served-model-name QwQ-32B \ --trust-remote-code \ --tensor-parallel-size 4 \ --max-model-len 30000 \ --port 8006 \ --reasoning-parser qwen3 \ response = client.chat.completions.create( model=model_name, messages=messages, temperature=0.3, top_p=0.8, max_tokens=4000, extra_body={"chat_template_kwargs": {"enable_thinking":False}}, )

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: EVICES=4,5,6,7 python3 -m vllm.entrypoints.openai.api_server \ --model $modelpath \ --served-model-name QwQ-32B \ --trust-remote-code \ --tensor-parallel-size 4 \ --max-model-len 30000 \ --port 8006 \ --reasoning-parser...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Doc]: can not close thinking documentation version=0.9.0.1 set enable_thinking=True , can not close thinking CUDA_VISIBLE_DEVICES=4,5,6,7 python3 -m vllm.entrypoints.openai.api_server \ --model $modelpath \ --served-mo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: n version=0.9.0.1 set enable_thinking=True , can not close thinking CUDA_VISIBLE_DEVICES=4,5,6,7 python3 -m vllm.entrypoints.openai.api_server \ --model $modelpath \ --served-model-name QwQ-32B \ --trust-remote-code \ -...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 00, extra_body={"chat_template_kwargs": {"enable_thinking":False}}, )

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

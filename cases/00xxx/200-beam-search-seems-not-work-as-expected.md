# vllm-project/vllm#200: Beam search seems not work as expected

| 字段 | 值 |
| --- | --- |
| Issue | [#200](https://github.com/vllm-project/vllm/issues/200) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Beam search seems not work as expected

### Issue 正文摘录

Hi, I try to use the beam search of vllm with the following code, but I found it processes and generates much more results than input, could anyone kindly tell me how to fix that? ``` model = LLM(model=args.model_name_or_path) prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] gen_params = SamplingParams(n=1, use_beam_search=True, best_of=5, temperature=0, top_p=1, top_k=-1, max_tokens=args.max_new_tokens, stop=[" "]) outputs = model.generate(prompts, gen_params) print(f"generate {len(outputs)} outputs!!!") ```

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: Beam search seems not work as expected bug Hi, I try to use the beam search of vllm with the following code, but I found it processes and generates much more results than input, could anyone kindly tell me how to fix th...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: re results than input, could anyone kindly tell me how to fix that? ``` model = LLM(model=args.model_name_or_path) prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

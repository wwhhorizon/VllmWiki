# vllm-project/vllm#780: baichuan-13b-base output is not same as hugginface transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#780](https://github.com/vllm-project/vllm/issues/780) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> baichuan-13b-base output is not same as hugginface transformers

### Issue 正文摘录

When prompt="请介绍深圳市"，temperature=1.0 top_k=1 top_p=1 and dtype = fp16. I find vllm (d1744376ae9fdbfa6a2dc763e1c67309e138fa3d) ouput text is "的经济状况,人口,交通,旅游,文化,教育,医疗,体育,环境,治安,消费,住房,就业,收入,物价,消费,天气,民族,宗教,语言,饮食,服饰,节日,习俗,禁忌,婚丧,礼仪,名胜,古迹,旅游,文化,教育,医疗,体育,环境,治安,消费,住房,就业,收入,物价,消费,天气,民族,宗教,语言,饮食,服饰,节日,习俗,禁忌,婚丧,礼仪,名胜,古迹,", but huggingface transformers's ouput text is " 的经济状况,人口,交通,旅游,文化,教育,医疗,体育,环境,治安,消费,住房,就业,物价,收入,民族,宗教,语言,饮食,服饰,节日,习俗,禁忌,婚丧,礼仪,名胜,古迹,旅游,文化,教育,医疗,体育,环境,治安,消费,住房,就业,物价,收入,民族,宗教,语言,饮食,服饰,节日,习俗,禁忌,婚丧,礼仪,名胜,古迹,旅游,文化,教育,医疗". But when dtype is fp32, the output text is all "的经济状况,谢谢! 深圳的经济状况 深圳经济特区建立以来,在短短的20多年里,深圳经济实现了跨越式发展,创造了举世瞩目的“深圳速度”。1980年,深圳国内生产总值仅为1.96亿元,2003年达到7800亿元,年均增长20.7%,是1980年的386倍。2003年,深圳人均GDP达到1.6万美元,是1980年的1000倍。 深圳经济"。 Comparing dozens prompts, this divergence of two library is always present.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: p_p=1 and dtype = fp16. I find vllm (d1744376ae9fdbfa6a2dc763e1c67309e138fa3d) ouput text is "的经济状况,人口,交通,旅游,文化,教育,医疗,体育,环境,治安,消费,住房,就业,收入,物价,消费,天气,民族,宗教,语言,饮食,服饰,节日,习俗,禁忌,婚丧,礼仪,名胜,古迹,旅游,文化,教育,医疗,体育,环境,治安,消费,住房,就业,收入,物价...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: 03年,深圳人均GDP达到1.6万美元,是1980年的1000倍。 深圳经济"。 Comparing dozens prompts, this divergence of two library is always present.
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ce transformers When prompt="请介绍深圳市"，temperature=1.0 top_k=1 top_p=1 and dtype = fp16. I find vllm (d1744376ae9fdbfa6a2dc763e1c67309e138fa3d) ouput text is "的经济状况,人口,交通,旅游,文化,教育,医疗,体育,环境,治安,消费,住房,就业,收入,物价,消费,天气,民族,宗教,语言...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 体育,环境,治安,消费,住房,就业,收入,物价,消费,天气,民族,宗教,语言,饮食,服饰,节日,习俗,禁忌,婚丧,礼仪,名胜,古迹,", but huggingface transformers's ouput text is " 的经济状况,人口,交通,旅游,文化,教育,医疗,体育,环境,治安,消费,住房,就业,物价,收入,民族,宗教,语言,饮食,服饰,节日,习俗,禁忌,婚丧,礼仪,名胜,古迹,旅游,文化,教育,医疗,体育,环境,治...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

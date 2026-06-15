# vllm-project/vllm#892: Why does the output first expand the question before starting to answer it?

| 字段 | 值 |
| --- | --- |
| Issue | [#892](https://github.com/vllm-project/vllm/issues/892) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why does the output first expand the question before starting to answer it?

### Issue 正文摘录

LLM model:Baichuan-13B-Chat GPU:TITAN RTX 24G tensor_parallel_size:2 vllm version:0.1.4 issue example: Prompt: '介绍一下广州的景点', Generated text: '**和美食\n**广州是中国的南部城市，拥有悠久的历史和丰富的文化。这里有很多著名的景点和美食，吸引了无数游客。以下是一些建议供您参考：\n\n景点：\n1. 广州塔(小蛮腰)：广州塔是广州的地标性建筑，高600米，您可以乘坐观光电梯到达塔顶，俯瞰整个广州市区的美景。\n2. 白云山：白云山是广州著名的自然风景区，山上绿树成荫，空气清新，您可以在这里欣赏美丽的自然风光，还可以参观寺庙、亭台楼阁等人文景观。\n3. 越秀公园：越秀公园是广州最大的公园之一，公园内有湖泊、亭台楼阁、花坛等景观，还有一座古老的五羊雕像，是广州市的象征。\n4. 陈家祠：陈家祠是广州著名的文化遗址，是一座具有岭南建筑风格的祠堂，内部装饰精美，展示了广州地区的传统文化。\n5. 广州长隆旅游度假区：长隆旅游度假区内有长隆野生动物园、长隆国际大马戏、长隆水上乐园等多个景点，是家庭旅游的好去处。\n\n美食：\n1. 早茶：广州早茶是广州当地的一种饮食文化，您可以在茶楼品尝各种点心，如虾饺、烧卖、肠粉等。\n2. 烧烤：广州的烧烤品种繁多，如烤鱼、烤鸡、烤肉等，口感鲜美，是夜宵的好选择。\n3. 糖水：广州的糖水是一种甜品，如双皮奶、芝麻糊、杨枝甘露等，口感细腻，味道香甜。\n4. 煲仔饭：广州的煲仔饭是一种特色美食，将饭菜放入砂锅中烹饪，味道鲜美，营养丰富。\n5. 广式月饼：广州的月饼品种繁多，如莲蓉月饼、五仁月饼、蛋黄月饼等，口感香甜，是中秋节的传统美食。\n\n希望这些建议能帮助您更好地了解广州的景点和美食，祝您在广州度过愉快的旅程！' Prompt: '狗子掉毛怎么办', Generated text: '**?\n**1. 定期给狗狗梳毛:每天为狗狗梳毛可以有效去除死皮和减少掉毛,同时还可以促进皮肤血液循环。\n\n2. 选择合适的洗浴产品:给狗狗选择适合敏感皮肤的洗浴产品,避免使用碱性强的洗浴用品,以免刺激皮肤导致掉毛。\n\n3. 定期洗澡:根据狗狗的实际情况,每隔一段时间给狗狗洗澡一次,保持皮肤清洁。\n\n4. 饮食健康:给狗狗提供营养均衡的食物,避免喂食含盐、油腻的食物,以免刺激皮肤导致掉毛。\n\n5. 保持室内干燥:避免让狗狗待在潮湿的环境中,以免皮肤病的发生。\n\n6. 定期检查皮肤:定期检查狗狗的皮肤,发现异常情况及时就医。\n\n7. 保持狗狗心情愉快:给狗狗提供足够的运动和娱乐,保持狗狗心情愉快,避免因焦虑、紧张等情绪导致掉毛。\n\n8. 选择适合的狗狗毛发护理产品:可以使...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: LM model:Baichuan-13B-Chat GPU:TITAN RTX 24G tensor_parallel_size:2 vllm version:0.1.4 issue example: Prompt: '介绍一下广州的景点', Generated text: '**和美食\n**广州是中国的南部城市，拥有悠久的历史和丰富的文化。这里有很多著名的景点和美食，吸引了无数游客。以下是一些建议供您参考：\n\n景点：\n1....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tion before starting to answer it? LLM model:Baichuan-13B-Chat GPU:TITAN RTX 24G tensor_parallel_size:2 vllm version:0.1.4 issue example: Prompt: '介绍一下广州的景点', Generated text: '**和美食\n**广州是中国的南部城市，拥有悠久的历史和丰富的文化。这里有很多著名的景...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s the output first expand the question before starting to answer it? LLM model:Baichuan-13B-Chat GPU:TITAN RTX 24G tensor_parallel_size:2 vllm version:0.1.4 issue example: Prompt: '介绍一下广州的景点', Generated text: '**和美食\n**...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

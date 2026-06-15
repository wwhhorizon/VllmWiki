# vllm-project/vllm#1643: baichuan-13b-chat用vllm来生成，很多测试数据（有长有短，没有超出长度限制）只能生成一个句号，而且有些示例在删掉一些字词或句子之后，就可以正常生成了，请问有可能是什么原因？

| 字段 | 值 |
| --- | --- |
| Issue | [#1643](https://github.com/vllm-project/vllm/issues/1643) |
| 状态 | closed |
| 标签 |  |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> baichuan-13b-chat用vllm来生成，很多测试数据（有长有短，没有超出长度限制）只能生成一个句号，而且有些示例在删掉一些字词或句子之后，就可以正常生成了，请问有可能是什么原因？

### Issue 正文摘录

baichuan-13b-chat用vllm来生成，很多测试数据（有长有短，没有超出长度限制）只能生成一个句号，而且有些示例在删掉一些字词或句子之后，就可以正常生成了，请问有可能是什么原因？ import torch from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0, top_p=1, max_tokens=512) prompts_list=["用户遇到问题前来求助客服，他们的对话内容如下：\n'''\n客服：您好，请问是咨询**功能的问题吗。\n用户：是的。\n客服：**的什么问题。\n用户：**问题。\n客服：是****什么。\n用户：我****，它说被多少用户举报打不开了。\n客服：****被封了对吗。\n用户：是的。\n客服：稍后，会给您来电手机绑定的微信，这是一个入口，您点击那个入口去提交一下被封的复审资料，由工作人员来进行核实的。\n用户：好的好的。\n客服：尽快提交一下，就不打扰您。\n'''\n请根据客服和用户的多轮对话，生成对话总结，总结内容包括两部分：\n1、问题描述：表示的是用户遇到的问题。\n2、客服方案：指的是客服提出的解决方案，如果用户不接受，客服会继续提出其他方案，每个方案都需要总结在“客服方案”部分。"] llm = LLM(model = './Baichuan-13B-Chat', trust_remote_code=True, dtype='float16', tensor_parallel_size=1) outputs=llm.generate(prompts_list, sampling_params) outputs[0].outputs[0].text 输出结果是一个句号 ![企业微信截图_16998783255972](https://github.com/vllm-project/vllm/assets/73767263/708db0fc-3dee-497d-a0d3-7d81a731f810)

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: 案”部分。"] llm = LLM(model = './Baichuan-13B-Chat', trust_remote_code=True, dtype='float16', tensor_parallel_size=1) outputs=llm.generate(prompts_list, sampling_params) outputs[0].outputs[0].text 输出结果是一个句号 ![企业微信截图_1699878...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 成，很多测试数据（有长有短，没有超出长度限制）只能生成一个句号，而且有些示例在删掉一些字词或句子之后，就可以正常生成了，请问有可能是什么原因？ import torch from vllm import LLM, SamplingParams sampling_params = SamplingParams(temperature=0, top_p=1, max_tokens=512) prompts_list=["用户遇到问题前来求...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: n2、客服方案：指的是客服提出的解决方案，如果用户不接受，客服会继续提出其他方案，每个方案都需要总结在“客服方案”部分。"] llm = LLM(model = './Baichuan-13B-Chat', trust_remote_code=True, dtype='float16', tensor_parallel_size=1) outputs=llm.generate(prompts_list, sampling_params...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

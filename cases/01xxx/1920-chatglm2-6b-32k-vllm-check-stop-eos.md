# vllm-project/vllm#1920: Chatglm2-6b-32k通过vLLM加速后，对话会出现异常终止的问题（但_check_stop函数中判断是eos正常终止）

| 字段 | 值 |
| --- | --- |
| Issue | [#1920](https://github.com/vllm-project/vllm/issues/1920) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Chatglm2-6b-32k通过vLLM加速后，对话会出现异常终止的问题（但_check_stop函数中判断是eos正常终止）

### Issue 正文摘录

Chatglm2-6b-32k通过vLLM加速后，对话会出现异常终止的问题（但_check_stop函数中判断是eos正常终止） 部署环境：使用 langchain_chatchat 0.2.7 + fastchat 0.2.32 + vllm 0.2.2 部署 SamplingParams采样参数：其他参数保持默认，repetition_penalty=1.2 #### 异常现象： 进行了三轮对话出现异常终止的现象 - 测试数据：Round1:你好 Round2:公司的信息安全体系如何? Round3:给我讲个故事 - 第三轮输出异常终止 ```bash 在很久以前的一个小村庄里，有一个聪明的少年叫李雷。他经常帮助村里的长老们解决各种难题,深受村里人的尊敬和信任。 有一天,一个神秘的人来到村子,他告诉村子的长老们:如果他们想要安全地保护村里的信息系统和数据,就必须采取一些措施来防止黑客攻击和维护网络的稳定性。 长老们听了这位客 ``` - 但是在`_check_stop`函数中预埋的print输出是遇到了eos结束符才终止的 #### 请问这是否是vllm对chatglm2的适配引发的异常？ #### 测试过程截图如下： ![5f80ad0bfbb100f74e3bf869c87197f](https://github.com/vllm-project/vllm/assets/24311412/efd97dba-7f37-4030-8b91-2e05d1d317a1) ![4dfaa2fbf0e947fa582823f069cc8f2](https://github.com/vllm-project/vllm/assets/24311412/964afe6c-a45a-4a40-bab6-69878e3fb833) ![038c427cb57cf1d66a1bb682cf0afd9](https://github.com/vllm-project/vllm/assets/24311412/b654ae6e-2832-4e18-96fd-784ced1998be)

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

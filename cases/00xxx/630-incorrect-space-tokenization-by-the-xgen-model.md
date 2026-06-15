# vllm-project/vllm#630: Incorrect space tokenization by the Xgen model

| 字段 | 值 |
| --- | --- |
| Issue | [#630](https://github.com/vllm-project/vllm/issues/630) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Incorrect space tokenization by the Xgen model

### Issue 正文摘录

Hi, When I run VLLM with the **Xgen** model, it **adds extra space** before few words. ``` What is the most promising ML tech coming out? It is hard to predict the most promising ML tech as it is a fast - paced field with new techniques and tools emerging frequently . However , some of the recent developments in ML that show a lot of promise are : 1 . Gener ative Pre - trained Trans former ( G PT ) family of models : The G PT model family , which includes G PT - 3 , G PT - 4 , and G PT - J , has been making headlines for its ability to generate human - like text . These models use the transformer architecture and have been pre - trained on large amounts of text data . They can be used for a variety of tasks such as text classification , generation , and summar ization . 2 . Auto ML : Auto ML refers to the use of automation to train models without requiring manual intervention . Companies like Google and Amazon have been investing in Auto ML to make it easier for users to train models without needing to have deep data science expertise . Auto ML can be used for a variety of tasks such as image classification , object detection , and time series forecasting . 3 . Mult ilingual and c...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: o generate human - like text . These models use the transformer architecture and have been pre - trained on large amounts of text data . They can be used for a variety of tasks such as text classification , generation ,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Incorrect space tokenization by the Xgen model bug Hi, When I run VLLM with the **Xgen** model, it **adds extra space** before few words. ``` What is the most promising ML tech coming out? It is hard to predict the most...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: for users to train models without needing to have deep data science expertise . Auto ML can be used for a variety of tasks such as image classification , object detection , and time series forecasting . 3 . Mult ilingua...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: izer.decode(token_cache ,skip_special_tokens=True) full_word = False cur_space = text.rfind(" ")+1 if cur_space!=previous_space: full_word = True previous_space = cur_space if len(text_cache)>0: data = {'token
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ers to train models without needing to have deep data science expertise . Auto ML can be used for a variety of tasks such as image classification , object detection , and time series forecasting . 3 . Mult ilingual and...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

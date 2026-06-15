# vllm-project/vllm#7558: [RFC]: Support for video input 

| 字段 | 值 |
| --- | --- |
| Issue | [#7558](https://github.com/vllm-project/vllm/issues/7558) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support for video input 

### Issue 正文摘录

### Motivation. Currently models like `llava-hf/llava-next-video*` recognize image and video inputs with different tokens, and do different computations. Therefore vLLM should provide new APIs and inference support for video input. ### Proposed Change. #### API * `LLM.generate()` API for video ```python LLM.generate({ "prompt": " please summarize this video", "multi_modal_data": { "video": video } }) ``` * [OpenAI compatible chat completion APIs](https://cookbook.openai.com/examples/gpt_with_vision_for_video_understanding) #### Roadmap * Add `VideoPlugin` for `MultiModalPlugin` * #7559 * Add initial support for replacing a \ token with a single video. * Add support for replacing all \ and \ tokens with multiple multi-modal inputs. * Support prefix caching for the same videos. * Support openai chat completion APIs. ### Feedback Period. A week ### CC List. @DarkLight1337 @zifeitong @ywang ### Any Other Things. _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: Support for video input RFC ### Motivation. Currently models like `llava-hf/llava-next-video*` recognize image and video inputs with different tokens, and do different computations. Therefore vLLM should provide...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lugin` for `MultiModalPlugin` * #7559 * Add initial support for replacing a \ token with a single video. * Add support for replacing all \ and \ tokens with multiple multi-modal inputs. * Support prefix caching for the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

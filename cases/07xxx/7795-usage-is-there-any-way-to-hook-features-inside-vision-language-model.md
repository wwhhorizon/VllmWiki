# vllm-project/vllm#7795: [Usage]: Is there any way to hook features inside vision-language model? 

| 字段 | 值 |
| --- | --- |
| Issue | [#7795](https://github.com/vllm-project/vllm/issues/7795) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Is there any way to hook features inside vision-language model? 

### Issue 正文摘录

### Your current environment # Initialize the LLaVA-1.5 model llm = LLM(model="llava-hf/llava-1.5-7b-hf") print(llm) #embed_last_hook = Hook(model.language_model.model.norm) # for save embed # Define the prompts and images base_p = '../../../data/detect/coco/train2017' img_p1 = os.path.join(base_p, '000000265292.jpg') img_p2 = os.path.join(base_p, '000000318124.jpg') img_p3 = os.path.join(base_p, '000000370121.jpg') prompts = [ {"prompt": "USER: \nWhat is the content of this image?\nASSISTANT:", "multi_modal_data": {"image": PIL.Image.open(img_p1)}}, {"prompt": "USER: \nWhat is the content of this image?\nASSISTANT:", "multi_modal_data": {"image": PIL.Image.open(img_p2)}}, {"prompt": "USER: \nWhat is the content of this image?\nASSISTANT:", "multi_modal_data": {"image": PIL.Image.open(img_p3)}} ] # Define sampling parameters sampling_params = SamplingParams(temperature=0.0, top_p=1.0) # Generate outputs outputs = llm.generate(prompts, sampling_params=sampling_params) I want to add hook some features when llm's forward finished how can i get feature inside? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: Is there any way to hook features inside vision-language model? usage;stale ### Your current environment # Initialize the LLaVA-1.5 model llm = LLM(model="llava-hf/llava-1.5-7b-hf") print(llm) #embed_last_hook...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: : Is there any way to hook features inside vision-language model? usage;stale ### Your current environment # Initialize the LLaVA-1.5 model llm = LLM(model="llava-hf/llava-1.5-7b-hf") print(llm) #embed_last_hook = Hook(...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

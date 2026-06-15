# vllm-project/vllm#11221: [Usage]: How to run intern_vit model using intern_vit.py?

| 字段 | 值 |
| --- | --- |
| Issue | [#11221](https://github.com/vllm-project/vllm/issues/11221) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to run intern_vit model using intern_vit.py?

### Issue 正文摘录

### Your current environment As far as i know,the Internvl series models use intern_vit.py to load vision module. In my case, i am wondering if the intern_vit.py can be used to load intern_vit models（only the vision part）. And how to use? Below is my python script: ``` from vllm import LLM, SamplingParams import time from transformers import CLIPImageProcessor def run_Internvit(): sampling_params = SamplingParams(max_tokens=100, temperature=0.8, top_p=0.95, top_k=1) llm = LLM(model="/mnt/beegfs/maojunxiong/Vision_vllm/internvl-6B", trust_remote_code=True) #tokenizer = AutoTokenizer.from_pretrained("/mnt/beegfs/maojunxiong/Vision_vllm/internvl-6B", trust_remote_code=True) image = Image.open('/mnt/beegfs/maojunxiong/Vision_vllm/image1.jpg').convert('RGB') #image_processor = CLIPImageProcessor.from_pretrained('/mnt/beegfs/maojunxiong/Vision_vllm/internvl-6B/') #pixel_values = image_processor(images=image, return_tensors='pt').pixel_values #pixel_values = pixel_values.to(torch.bfloat16).cuda() outputs = [] outputs = llm.generate(image, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].text token = len(tokenizer.encode(generated_text)) to...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: How to run intern_vit model using intern_vit.py? usage;stale ### Your current environment As far as i know,the Internvl series models use intern_vit.py to load vision module. In my case, i am wondering if the i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vision part）. And how to use? Below is my python script: ``` from vllm import LLM, SamplingParams import time from transformers import CLIPImageProcessor def run_Internvit(): sampling_params = SamplingParams(max_tokens=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: urn_tensors='pt').pixel_values #pixel_values = pixel_values.to(torch.bfloat16).cuda() outputs = [] outputs = llm.generate(image, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.out...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: s='pt').pixel_values #pixel_values = pixel_values.to(torch.bfloat16).cuda() outputs = [] outputs = llm.generate(image, sampling_params) for output in outputs: prompt = output.prompt generated_text = output.outputs[0].te...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to run intern_vit model using intern_vit.py? usage;stale ### Your current environment As far as i know,the Internvl series models use intern_vit.py to load vision module. In my case, i am wondering if the i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。

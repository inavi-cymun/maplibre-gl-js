import {createLayout} from '../../util/struct_array';

const layout = createLayout([
    {name: 'a_pos3d', components: 3, type: 'Int16'}
], 4);

export default layout;
export const {members, size, alignment} = layout;
